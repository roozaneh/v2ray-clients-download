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
APPS_DIR = os.path.join(WORKSPACE_DIR, "apps")

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
        ],
        "link_pattern": r"https://github\.com/2dust/v2rayNG/releases/download/[^/]+/[^\s\"\'><\)]*_universal\.apk"
    },
    "Happ": {
        "repo": "Happ-proxy/happ-android",
        "patterns": [
            r"^Happ\.apk$",
            r"^Happ.*\.apk$"
        ],
        "link_pattern": r"https://github\.com/Happ-proxy/happ-android/releases/download/[^/]+/Happ\.apk"
    },
    "NekoBox": {
        "repo": "MatsuriDayo/NekoBoxForAndroid",
        "patterns": [
            r"^NekoBox-.*universal\.apk$",
            r"^NekoBox-.*arm64-v8a\.apk$"
        ],
        "link_pattern": r"https://github\.com/MatsuriDayo/NekoBoxForAndroid/releases/download/[^/]+/NekoBox-[^\s\"\'><\)]*-arm64-v8a\.apk"
    },
    "SingBox": {
        "repo": "SagerNet/sing-box",
        "patterns": [
            r"^SFA-[\d\.]+-universal\.apk$",
            r"^SFA-.*(?<!legacy-)universal\.apk$",
            r"^SFA-.*universal\.apk$",
            r"^SFA-.*arm64-v8a\.apk$"
        ],
        "link_pattern": r"https://github\.com/SagerNet/sing-box/releases/download/[^/]+/SFA-[^\s\"\'><\)]*-universal\.apk"
    },
    "Hiddify_Android": {
        "repo": "hiddify/hiddify-app",
        "patterns": [
            r"^Hiddify-Android-universal\.apk$",
            r"^Hiddify-Android-arm64\.apk$"
        ],
        "link_pattern": r"https://github\.com/hiddify/hiddify-app/releases/download/[^/]+/Hiddify-Android-universal\.apk"
    },
    "Hiddify_Windows": {
        "repo": "hiddify/hiddify-app",
        "patterns": [
            r"^Hiddify-Windows-Setup-x64\.exe$",
            r"^Hiddify-Windows-.*\.exe$",
            r"^Hiddify-Windows-.*\.zip$"
        ],
        "link_pattern": r"https://github\.com/hiddify/hiddify-app/releases/download/[^/]+/Hiddify-Windows-Setup-x64\.exe"
    },
    "v2rayN": {
        "repo": "2dust/v2rayN",
        "patterns": [
            r"^v2rayN-windows-64\.zip$",
            r"^v2rayN-With-Core\.zip$"
        ],
        "link_pattern": r"https://github\.com/2dust/v2rayN/releases/download/[^/]+/v2rayN-windows-64\.zip"
    },
    "NekoRay": {
        "repo": "MatsuriDayo/nekoray",
        "patterns": [
            r"^nekoray-.*windows64\.zip$",
            r"^nekoray-.*\.zip$"
        ],
        "link_pattern": r"https://github\.com/MatsuriDayo/nekoray/releases/download/[^/]+/nekoray-[^\s\"\'><\)]*-windows64\.zip"
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
        pattern = TARGETS.get(key, {}).get("link_pattern")
        if pattern:
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
        pattern = TARGETS.get(key, {}).get("link_pattern")
        if pattern:
            content = re.sub(pattern, url, content)

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated index.html direct links")


def update_apps_html(results):
    if not os.path.exists(APPS_DIR):
        return

    import glob
    app_files = glob.glob(os.path.join(APPS_DIR, "*.html"))
    for app_path in app_files:
        with open(app_path, "r", encoding="utf-8") as f:
            content = f.read()

        changed = False
        for key, info in results.items():
            url = info["download_url"]
            pattern = TARGETS.get(key, {}).get("link_pattern")
            if pattern:
                new_content = re.sub(pattern, url, content)
                if new_content != content:
                    content = new_content
                    changed = True

        if changed:
            with open(app_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {os.path.basename(app_path)} direct links")


if __name__ == "__main__":
    resolved = resolve_all_assets()
    if resolved:
        update_json(resolved)
        update_readme(resolved)
        update_html(resolved)
        update_apps_html(resolved)
        print("Synchronization completed successfully.")
    else:
        print("No releases resolved. Aborting update.")
        sys.exit(1)
