#!/usr/bin/env python3
"""
Automated Release Asset Fetcher & Link Synchronizer for Roozaneh Net
Fetches latest release tags & direct asset download URLs from official upstream repos,
and synchronizes README.md, index.html, and releases.json.
"""

import os
import sys
import re
import json
import urllib.request
from datetime import datetime, timezone

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(WORKSPACE_DIR, "README.md")
HTML_PATH = os.path.join(WORKSPACE_DIR, "index.html")
JSON_PATH = os.path.join(WORKSPACE_DIR, "releases.json")

# GitHub Token resolution
TOKEN = os.environ.get("GITHUB_TOKEN")
SECRET_PATH = "/home/hokar/.gemini/antigravity/private_docs/rozaneh/github.secret.json"
if not TOKEN and os.path.exists(SECRET_PATH):
    try:
        with open(SECRET_PATH, "r", encoding="utf-8") as f:
            TOKEN = json.load(f).get("token")
    except Exception:
        pass

HEADERS = {
    "User-Agent": "Roozaneh-Auto-Updater/1.0",
    "Accept": "application/vnd.github.v3+json"
}
if TOKEN:
    HEADERS["Authorization"] = f"token {TOKEN}"

# Configured targets
TARGETS = {
    "v2rayNG": {
        "repo": "2dust/v2rayNG",
        "patterns": [
            r"^v2rayNG_.*(?<!fdroid)_universal\.apk$",
            r"^v2rayNG_.*universal\.apk$",
            r"^v2rayNG_.*arm64-v8a\.apk$"
        ]
    },
    "Happ": {
        "repo": "Happ-proxy/happ-android",
        "patterns": [
            r"^Happ\.apk$",
            r"^Happ.*\.apk$"
        ]
    },
    "NekoBox": {
        "repo": "MatsuriDayo/NekoBoxForAndroid",
        "patterns": [
            r"^NekoBox-.*universal\.apk$",
            r"^NekoBox-.*arm64-v8a\.apk$"
        ]
    },
    "SingBox": {
        "repo": "SagerNet/sing-box",
        "patterns": [
            r"^SFA-.*universal\.apk$",
            r"^SFA-.*arm64-v8a\.apk$"
        ]
    },
    "Hiddify_Android": {
        "repo": "hiddify/hiddify-app",
        "patterns": [
            r"^Hiddify-Android-universal\.apk$",
            r"^Hiddify-Android-arm64\.apk$"
        ]
    },
    "Hiddify_Windows": {
        "repo": "hiddify/hiddify-app",
        "patterns": [
            r"^Hiddify-Windows-Setup-x64\.exe$",
            r"^Hiddify-Windows-.*\.exe$",
            r"^Hiddify-Windows-.*\.zip$"
        ]
    },
    "v2rayN": {
        "repo": "2dust/v2rayN",
        "patterns": [
            r"^v2rayN-windows-64\.zip$",
            r"^v2rayN-With-Core\.zip$"
        ]
    },
    "NekoRay": {
        "repo": "MatsuriDayo/nekoray",
        "patterns": [
            r"^nekoray-.*windows64\.zip$",
            r"^nekoray-.*\.zip$"
        ]
    }
}


def fetch_latest_release(repo):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def resolve_all_assets():
    results = {}
    print(f"[{datetime.now(timezone.utc).isoformat()}] Starting release synchronization...")
    for key, cfg in TARGETS.items():
        repo = cfg["repo"]
        patterns = cfg["patterns"]
        try:
            data = fetch_latest_release(repo)
            tag = data.get("tag_name", "")
            assets = data.get("assets", [])
            matched = None

            for pattern in patterns:
                for a in assets:
                    name = a.get("name", "")
                    if name.endswith(".sig"):
                        continue
                    if re.match(pattern, name, re.IGNORECASE):
                        matched = a
                        break
                if matched:
                    break

            if matched:
                results[key] = {
                    "repo": repo,
                    "tag": tag,
                    "asset_name": matched["name"],
                    "download_url": matched["browser_download_url"],
                    "size_mb": round(matched.get("size", 0) / (1024 * 1024), 2),
                    "updated_at": matched.get("updated_at", "")
                }
                print(f"✓ {key}: {tag} -> {matched['name']} ({results[key]['size_mb']} MB)")
            else:
                print(f"⚠️ {key}: No asset matching patterns in {repo}")
        except Exception as e:
            print(f"❌ Error fetching {key} ({repo}): {e}")

    return results


def update_json(results):
    payload = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "clients": results
    }
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Saved {JSON_PATH}")


def update_readme(results):
    if not os.path.exists(README_PATH):
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace specific download links if present
    for key, info in results.items():
        url = info["download_url"]
        tag = info["tag"]
        # Replace marker-based or specific pattern URLs
        # e.g. https://github.com/2dust/v2rayNG/releases/download/...
        repo_prefix = info["repo"]
        pattern = rf"https://github\.com/{re.escape(repo_prefix)}/releases/download/[^\s\)\"\'>]+"
        content = re.sub(pattern, url, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated README.md direct links")


def update_html(results):
    if not os.path.exists(HTML_PATH):
        return

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    for key, info in results.items():
        url = info["download_url"]
        repo_prefix = info["repo"]
        # Replace download hrefs for that repo
        pattern = rf"https://github\.com/{re.escape(repo_prefix)}/releases/download/[^\s\"\'><]+"
        content = re.sub(pattern, url, content)
        # Also replace release page link if on direct download button
        # e.g. href="https://github.com/2dust/v2rayNG/releases" -> href="{url}"

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated index.html direct links")


if __name__ == "__main__":
    resolved = resolve_all_assets()
    if resolved:
        update_json(resolved)
        update_readme(resolved)
        update_html(resolved)
        print("Synchronization completed successfully.")
    else:
        print("No releases resolved. Aborting update.")
        sys.exit(1)
