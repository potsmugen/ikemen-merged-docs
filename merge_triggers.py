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

    # Parse all documents
    mugen = parse_sections(mugen_text)
    changed = parse_sections(changed_text)
    new = parse_sections(new_text)

    # --- REMOVE REDIRECTION SECTIONS (they go to the redirections page) ---

    # Remove any sections that contain "redirection" in their name (M.U.G.E.N)
    for key in list(mugen.keys()):
        if "redirection" in key.lower():
            mugen.pop(key, None)

    # Remove the entire "Changed trigger redirections" block (stored as one key)
    changed.pop("Changed trigger redirections", None)
    # Also remove any other stray redirection sections (just in case)
    for key in list(changed.keys()):
        if "redirection" in key.lower():
            changed.pop(key, None)

    # Remove "New trigger redirections" from new page
    new.pop("New trigger redirections", None)

    # --- EXTRACT INDIVIDUAL TRIGGERS FROM "New triggers" ---
    new_individual = {}
    if "New triggers" in new:
        triggers_block = new.pop("New triggers")
        new_individual = parse_sub_sections(triggers_block)

    # --- RENAME CHANGED SECTIONS ---
    changed = rename_changed_sections(changed, suffix="(changed)")

    # --- MERGE ---
    merged = merge_sections([
        ("M.U.G.E.N 1.1", mugen),
        ("Ikemen GO (changed)", changed),
        ("Ikemen GO (new)", new_individual),
    ])

    print(f"Merged {len(merged)} trigger sections.", file=sys.stderr)

    # --- OUTPUT ---
    output = output_merged(
        merged,
        "Merged Trigger Reference",
        sections_to_skip=[],
        top_sections=[]
    )

    output_file = Path("docs/triggers.md")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(output, encoding="utf-8")
    print(f"\nDone. Output saved to: {output_file}", file=sys.stderr)
    print(f"  {len(merged)} trigger sections merged.", file=sys.stderr)


if __name__ == "__main__":
    main()