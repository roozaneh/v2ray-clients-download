#!/usr/bin/env python3
"""
Automated Release Asset Fetcher & Link Synchronizer for Roozaneh Net
Fetches latest release tags & direct asset download URLs from official upstream repos,
and synchronizes README.md, index.html, releases.json, and apps/*.html (primary + secondary builds).
"""

import glob
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(WORKSPACE_DIR, "README.md")
HTML_PATH = os.path.join(WORKSPACE_DIR, "index.html")
JSON_PATH = os.path.join(WORKSPACE_DIR, "releases.json")
APPS_DIR = os.path.join(WORKSPACE_DIR, "apps")

# GitHub Token resolution (env var first, then optional local secret path via env fallback)
TOKEN = os.environ.get("GITHUB_TOKEN")
DEFAULT_SECRET_PATH = os.path.join(
    os.path.expanduser("~"),
    ".gemini",
    "antigravity",
    "private_docs",
    "rozaneh",
    "github.secret.json",
)
SECRET_PATH = os.environ.get("ROOZANEH_GITHUB_SECRET_PATH", DEFAULT_SECRET_PATH)
if not TOKEN and SECRET_PATH and os.path.exists(SECRET_PATH):
    try:
        with open(SECRET_PATH, "r", encoding="utf-8") as f:
            TOKEN = json.load(f).get("token")
    except Exception:
        pass

HEADERS = {
    "User-Agent": "Roozaneh-Auto-Updater/1.1",
    "Accept": "application/vnd.github.v3+json",
}
if TOKEN:
    HEADERS["Authorization"] = f"token {TOKEN}"

# Primary targets (persisted to releases.json and matched across HTML/README)
TARGETS = {
    "v2rayNG": {
        "repo": "2dust/v2rayNG",
        "patterns": [
            r"^v2rayNG_.*(?<!fdroid)_universal\.apk$",
            r"^v2rayNG_.*universal\.apk$",
            r"^v2rayNG_.*arm64-v8a\.apk$",
        ],
        "link_pattern": r"https://github\.com/2dust/v2rayNG/releases/download/[^/]+/[^\s\"\'><\)]*_universal\.apk",
    },
    "Happ": {
        "repo": "Happ-proxy/happ-android",
        "patterns": [
            r"^Happ\.apk$",
            r"^Happ.*\.apk$",
        ],
        "link_pattern": r"https://github\.com/Happ-proxy/happ-android/releases/download/[^/]+/Happ\.apk",
    },
    "NekoBox": {
        "repo": "MatsuriDayo/NekoBoxForAndroid",
        "patterns": [
            r"^NekoBox-.*universal\.apk$",
            r"^NekoBox-.*arm64-v8a\.apk$",
        ],
        "link_pattern": r"https://github\.com/MatsuriDayo/NekoBoxForAndroid/releases/download/[^/]+/NekoBox-[^\s\"\'><\)]*-arm64-v8a\.apk",
    },
    "SingBox": {
        "repo": "SagerNet/sing-box",
        "patterns": [
            r"^SFA-[\d\.]+-universal\.apk$",
            r"^SFA-.*(?<!legacy-)universal\.apk$",
            r"^SFA-.*universal\.apk$",
            r"^SFA-.*arm64-v8a\.apk$",
        ],
        "link_pattern": r"https://github\.com/SagerNet/sing-box/releases/download/[^/]+/SFA-[^\s\"\'><\)]*-universal\.apk",
    },
    "Hiddify_Android": {
        "repo": "hiddify/hiddify-app",
        "patterns": [
            r"^Hiddify-Android-universal\.apk$",
            r"^Hiddify-Android-arm64\.apk$",
        ],
        "link_pattern": r"https://github\.com/hiddify/hiddify-app/releases/download/[^/]+/Hiddify-Android-universal\.apk",
    },
    "Hiddify_Windows": {
        "repo": "hiddify/hiddify-app",
        "patterns": [
            r"^Hiddify-Windows-Setup-x64\.exe$",
            r"^Hiddify-Windows-.*\.exe$",
            r"^Hiddify-Windows-.*\.zip$",
        ],
        "link_pattern": r"https://github\.com/hiddify/hiddify-app/releases/download/[^/]+/Hiddify-Windows-Setup-x64\.exe",
    },
    "v2rayN": {
        "repo": "2dust/v2rayN",
        "patterns": [
            r"^v2rayN-windows-64\.zip$",
            r"^v2rayN-With-Core\.zip$",
        ],
        "link_pattern": r"https://github\.com/2dust/v2rayN/releases/download/[^/]+/v2rayN-windows-64\.zip",
    },
    "NekoRay": {
        "repo": "MatsuriDayo/nekoray",
        "patterns": [
            r"^nekoray-.*windows64\.zip$",
            r"^nekoray-.*\.zip$",
        ],
        "link_pattern": r"https://github\.com/MatsuriDayo/nekoray/releases/download/[^/]+/nekoray-[^\s\"\'><\)]*-windows64\.zip",
    },
}

# Secondary architecture/platform builds (synced across apps/*.html and any matching files)
SECONDARY_TARGETS = {
    "v2rayNG_arm64": {
        "repo": "2dust/v2rayNG",
        "patterns": [r"^v2rayNG_.*(?<!fdroid)_arm64-v8a\.apk$", r"^v2rayNG_.*_arm64-v8a\.apk$"],
        "link_pattern": r"https://github\.com/2dust/v2rayNG/releases/download/[^/]+/[^\s\"\'><\)]*_arm64-v8a\.apk",
    },
    "v2rayNG_armeabi": {
        "repo": "2dust/v2rayNG",
        "patterns": [r"^v2rayNG_.*(?<!fdroid)_armeabi-v7a\.apk$", r"^v2rayNG_.*_armeabi-v7a\.apk$"],
        "link_pattern": r"https://github\.com/2dust/v2rayNG/releases/download/[^/]+/[^\s\"\'><\)]*_armeabi-v7a\.apk",
    },
    "v2rayNG_x86_64": {
        "repo": "2dust/v2rayNG",
        "patterns": [r"^v2rayNG_.*(?<!fdroid)_x86_64\.apk$", r"^v2rayNG_.*_x86_64\.apk$"],
        "link_pattern": r"https://github\.com/2dust/v2rayNG/releases/download/[^/]+/[^\s\"\'><\)]*_x86_64\.apk",
    },
    "Happ_beta": {
        "repo": "Happ-proxy/happ-android",
        "patterns": [r"^Happ_beta\.apk$"],
        "link_pattern": r"https://github\.com/Happ-proxy/happ-android/releases/download/[^/]+/Happ_beta\.apk",
    },
    "NekoBox_armeabi": {
        "repo": "MatsuriDayo/NekoBoxForAndroid",
        "patterns": [r"^NekoBox-.*armeabi-v7a\.apk$"],
        "link_pattern": r"https://github\.com/MatsuriDayo/NekoBoxForAndroid/releases/download/[^/]+/NekoBox-[^\s\"\'><\)]*-armeabi-v7a\.apk",
    },
    "NekoBox_x86_64": {
        "repo": "MatsuriDayo/NekoBoxForAndroid",
        "patterns": [r"^NekoBox-.*x86_64\.apk$"],
        "link_pattern": r"https://github\.com/MatsuriDayo/NekoBoxForAndroid/releases/download/[^/]+/NekoBox-[^\s\"\'><\)]*-x86_64\.apk",
    },
    "SingBox_arm64": {
        "repo": "SagerNet/sing-box",
        "patterns": [r"^SFA-[\d\.]+-arm64-v8a\.apk$", r"^SFA-.*(?<!legacy-)arm64-v8a\.apk$"],
        "link_pattern": r"https://github\.com/SagerNet/sing-box/releases/download/[^/]+/SFA-[^\s\"\'><\)]*-arm64-v8a\.apk",
    },
    "SingBox_armeabi": {
        "repo": "SagerNet/sing-box",
        "patterns": [r"^SFA-[\d\.]+-armeabi-v7a\.apk$", r"^SFA-.*(?<!legacy-)armeabi-v7a\.apk$"],
        "link_pattern": r"https://github\.com/SagerNet/sing-box/releases/download/[^/]+/SFA-[^\s\"\'><\)]*-armeabi-v7a\.apk",
    },
    "Hiddify_Windows_Portable": {
        "repo": "hiddify/hiddify-app",
        "patterns": [r"^Hiddify-Windows-Portable-x64\.zip$"],
        "link_pattern": r"https://github\.com/hiddify/hiddify-app/releases/download/[^/]+/Hiddify-Windows-Portable-x64\.zip",
    },
    "Hiddify_macOS": {
        "repo": "hiddify/hiddify-app",
        "patterns": [r"^Hiddify-MacOS-Installer\.pkg$", r"^Hiddify-MacOS.*\.pkg$"],
        "link_pattern": r"https://github\.com/hiddify/hiddify-app/releases/download/[^/]+/Hiddify-MacOS[^\s\"\'><\)]*\.pkg",
    },
    "Hiddify_Linux": {
        "repo": "hiddify/hiddify-app",
        "patterns": [r"^Hiddify-Linux-x64\.AppImage$"],
        "link_pattern": r"https://github\.com/hiddify/hiddify-app/releases/download/[^/]+/Hiddify-Linux-x64\.AppImage",
    },
    "v2rayN_windows_desktop": {
        "repo": "2dust/v2rayN",
        "patterns": [r"^v2rayN-windows-64-desktop\.zip$"],
        "link_pattern": r"https://github\.com/2dust/v2rayN/releases/download/[^/]+/v2rayN-windows-64-desktop\.zip",
    },
    "v2rayN_windows_86": {
        "repo": "2dust/v2rayN",
        "patterns": [r"^v2rayN-windows-86\.zip$"],
        "link_pattern": r"https://github\.com/2dust/v2rayN/releases/download/[^/]+/v2rayN-windows-86\.zip",
    },
    "v2rayN_macos_arm64": {
        "repo": "2dust/v2rayN",
        "patterns": [r"^v2rayN-macos-arm64\.dmg$"],
        "link_pattern": r"https://github\.com/2dust/v2rayN/releases/download/[^/]+/v2rayN-macos-arm64\.dmg",
    },
    "NekoRay_debian": {
        "repo": "MatsuriDayo/nekoray",
        "patterns": [r"^nekoray-.*debian-x64\.deb$"],
        "link_pattern": r"https://github\.com/MatsuriDayo/nekoray/releases/download/[^/]+/nekoray-[^\s\"\'><\)]*-debian-x64\.deb",
    },
    "NekoRay_linux": {
        "repo": "MatsuriDayo/nekoray",
        "patterns": [r"^nekoray-.*linux64\.zip$"],
        "link_pattern": r"https://github\.com/MatsuriDayo/nekoray/releases/download/[^/]+/nekoray-[^\s\"\'><\)]*-linux64\.zip",
    },
}


def fetch_latest_release(repo, cache):
    if repo in cache:
        return cache[repo]
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    cache[repo] = data
    return data


def match_asset(assets, patterns):
    for pattern in patterns:
        for asset in assets:
            name = asset.get("name", "")
            if name.endswith(".sig"):
                continue
            if re.match(pattern, name, re.IGNORECASE):
                return asset
    return None


def resolve_all_assets():
    primary_results = {}
    replacements = []
    repo_cache = {}
    print(f"[{datetime.now(timezone.utc).isoformat()}] Starting release synchronization...")

    for key, cfg in TARGETS.items():
        repo = cfg["repo"]
        try:
            data = fetch_latest_release(repo, repo_cache)
            tag = data.get("tag_name", "")
            matched = match_asset(data.get("assets", []), cfg["patterns"])
            if matched:
                primary_results[key] = {
                    "repo": repo,
                    "tag": tag,
                    "asset_name": matched["name"],
                    "download_url": matched["browser_download_url"],
                    "size_mb": round(matched.get("size", 0) / (1024 * 1024), 2),
                    "updated_at": matched.get("updated_at", ""),
                }
                replacements.append((cfg["link_pattern"], matched["browser_download_url"]))
                print(f"✓ {key}: {tag} -> {matched['name']} ({primary_results[key]['size_mb']} MB)")
            else:
                print(f"⚠️ {key}: No asset matching patterns in {repo}")
        except Exception as e:
            print(f"❌ Error fetching {key} ({repo}): {e}")

    for key, cfg in SECONDARY_TARGETS.items():
        repo = cfg["repo"]
        try:
            data = fetch_latest_release(repo, repo_cache)
            matched = match_asset(data.get("assets", []), cfg["patterns"])
            if matched:
                replacements.append((cfg["link_pattern"], matched["browser_download_url"]))
                print(f"  ↳ {key}: {matched['name']}")
        except Exception as e:
            print(f"⚠️ Secondary target {key} ({repo}) skipped: {e}")

    return primary_results, replacements


def apply_replacements_to_file(file_path, replacements, label):
    if not os.path.exists(file_path):
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    for pattern, url in replacements:
        new_content = re.sub(pattern, url, new_content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {label} direct links")
        return True
    return False


def update_json(results):
    payload = {
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "clients": results,
    }
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Saved {JSON_PATH}")


def update_readme(replacements):
    apply_replacements_to_file(README_PATH, replacements, "README.md")


def update_html(replacements):
    apply_replacements_to_file(HTML_PATH, replacements, "index.html")


def update_apps_html(replacements):
    if not os.path.exists(APPS_DIR):
        return
    for app_path in sorted(glob.glob(os.path.join(APPS_DIR, "*.html"))):
        apply_replacements_to_file(app_path, replacements, os.path.basename(app_path))


if __name__ == "__main__":
    resolved, all_replacements = resolve_all_assets()
    if resolved:
        update_json(resolved)
        update_readme(all_replacements)
        update_html(all_replacements)
        update_apps_html(all_replacements)
        print("Synchronization completed successfully.")
    else:
        print("No releases resolved. Aborting update.")
        sys.exit(1)
