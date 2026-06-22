#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge M.U.G.E.N 1.1 + Ikemen GO Triggers.
"""

import sys
from pathlib import Path
from merge_lib import *


def main():
    print("=" * 60, file=sys.stderr)
    print("MERGED TRIGGERS", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    # Sources
    mugen_file = Path("triggers_mugen11.md")
    if not mugen_file.exists():
        print(f"ERROR: {mugen_file} not found", file=sys.stderr)
        sys.exit(1)

    mugen_text = load_file(mugen_file)

    changed_url = "https://raw.githubusercontent.com/wiki/ikemen-engine/Ikemen-GO/Triggers-(changed).md"
    new_url = "https://raw.githubusercontent.com/wiki/ikemen-engine/Ikemen-GO/Triggers-(new).md"

    print("Fetching Ikemen GO (changed)...", file=sys.stderr)
    changed_text = fetch_raw_markdown(changed_url)

    print("Fetching Ikemen GO (new)...", file=sys.stderr)
    new_text = fetch_raw_markdown(new_url)

    # Parse sections
    mugen = parse_sections(mugen_text)
    changed = parse_sections(changed_text)
    new = parse_sections(new_text)

    # Rename changed sections (e.g., "Triggers (changed)" sections)
    changed = rename_changed_sections(changed, suffix="(changed)")

    # Skip feature sections
    skip = {"New trigger redirections", "New triggers"}

    # Remove the new page's intro section from the merged result
    new.pop("New trigger redirections", None)
    new.pop("New triggers", None)

    # Merge
    merged = merge_sections([
        ("M.U.G.E.N 1.1", mugen),
        ("Ikemen GO (changed)", changed),
        ("Ikemen GO (new)", new),
    ])

    print(f"Merged {len(merged)} sections.", file=sys.stderr)

    output = output_merged(merged, "Merged Trigger Reference", skip)

    output_file = Path("triggers_merged.md")
    output_file.write_text(output, encoding="utf-8")
    print(f"\nDone. Output saved to: {output_file}", file=sys.stderr)
    print(f"  {len(merged)} sections merged.", file=sys.stderr)


if __name__ == "__main__":
    main()