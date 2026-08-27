#!/usr/bin/env python3
"""Verify local src/href references in HTML files resolve to real files."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_FILES = [ROOT / "index.html", ROOT / "resume.html"]
LOCAL_ATTR_PATTERN = re.compile(r'(?:src|href)=["\'](?!https?://|mailto:|tel:|javascript:|data:|#)([^"\']+)["\']', re.I)

STALE_TERMS = [
    "Home Depot",
    "iNautix",
    "Sybrant",
    "pcf",
    "neo4j",
    "Cloud Foundry",
    "Pivotal",
]

REQUIRED_TERMS = [
    "National Science Foundation (PES)",
    "Research.gov / FastLane",
    "USPTO",
    "Comcast",
    "HCL America",
    "Wenova",
    "British Sky Broadcasting",
    "Tata Teleservices",
    "Test Automation",
    "Performance & Security",
    "Accessibility (Section 508)",
    "Mobile Testing",
    "Languages & Scripting",
    "CI/CD & Build",
    "Test & Project Management",
    "Databases & Monitoring",
    "AI-Assisted Engineering",
    "Bachelor of Technology",
]


def main() -> int:
    errors: list[str] = []
    index_text = html.unescape((ROOT / "index.html").read_text(encoding="utf-8"))

    for html_path in HTML_FILES:
        if not html_path.exists():
            errors.append(f"Missing HTML file: {html_path.relative_to(ROOT)}")
            continue

        text = html_path.read_text(encoding="utf-8")
        for match in LOCAL_ATTR_PATTERN.findall(text):
            target = match.split("#")[0].split("?")[0]
            if not target or target.endswith("/"):
                continue
            resolved = (html_path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{html_path.name}: broken reference -> {target}")

    for term in STALE_TERMS:
        if term.lower() in index_text.lower():
            errors.append(f"Stale content found on index.html: {term}")

    for term in REQUIRED_TERMS:
        if term not in index_text:
            errors.append(f"Missing required content on index.html: {term}")

    if errors:
        print("Verification FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Verification passed.")
    print(f"  Checked {len(HTML_FILES)} HTML files")
    print(f"  Confirmed {len(REQUIRED_TERMS)} required terms present")
    print(f"  Confirmed no stale employer references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
