#!/usr/bin/env python3
"""
Legacy entrypoint wrapper — delegates to build_app_pages.py so both scripts
generate the exact same unified Apple Light apps/*.html files.
"""
from build_app_pages import main

if __name__ == "__main__":
    main()
