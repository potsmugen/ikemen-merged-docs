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

    # Parse all documents (parse_sections automatically handles HTML in headings)
    mugen = parse_sections(mugen_text)
    changed = parse_sections(changed_text)
    new = parse_sections(new_text)

    # --- FILTER OUT REDIRECTIONS ---
    # Remove redirection sections from M.U.G.E.N (they go to the redirections page)
    for key in list(mugen.keys()):
        if "redirection" in key.lower():
            mugen.pop(key, None)

    # Remove redirection sections from changed (if any)
    for key in list(changed.keys()):
        if "redirection" in key.lower():
            changed.pop(key, None)

    # Extract ONLY the individual triggers from the "New triggers" block
    new_individual = {}
    if "New triggers" in new:
        triggers_block = new.pop("New triggers")
        new_individual = parse_sub_sections(triggers_block)

    # Discard "New trigger redirections" from the new page if it exists
    new.pop("New trigger redirections", None)

    # --- RENAME CHANGED SECTIONS ---
    # e.g., "Anim triggers" becomes "Anim (changed)"
    changed = rename_changed_sections(changed, suffix="(changed)")

    # --- MERGE ---
    # Merge only pure triggers (redirections are handled by merge_redirections.py)
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