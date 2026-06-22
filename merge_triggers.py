#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge M.U.G.E.N 1.1 + Ikemen GO Triggers.

The "new" page has two parts:
- "New trigger redirections" → moved to the top as a dedicated section (content only)
- "New triggers" → individual triggers merged alphabetically with the rest
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

    # Parse the new page differently – we want to keep the redirections section intact,
    # but extract individual triggers from the "New triggers" block
    new_sections = parse_sections(new_text)

    # Separate "New trigger redirections"
    new_redirections = {}
    if "New trigger redirections" in new_sections:
        new_redirections["New trigger redirections"] = new_sections.pop("New trigger redirections")

    # Extract individual triggers from "New triggers"
    new_individual = {}
    if "New triggers" in new_sections:
        triggers_block = new_sections.pop("New triggers")
        # The content of "New triggers" contains individual triggers with ## headings
        # Extract them using parse_sub_sections
        new_individual = parse_sub_sections(triggers_block)

    # Rename changed sections
    changed = rename_changed_sections(changed, suffix="(changed)")

    # Merge all individual triggers
    merged = merge_sections([
        ("M.U.G.E.N 1.1", mugen),
        ("Ikemen GO (changed)", changed),
        ("Ikemen GO (new)", new_individual),
    ])

    print(f"Merged {len(merged)} sections.", file=sys.stderr)

    # Output
    # top_sections: "New trigger redirections" at the top (content only)
    output = output_merged(
        merged,
        "Merged Trigger Reference",
        sections_to_skip=[],
        top_sections=["New trigger redirections"]
    )

    output_file = Path("triggers.md")
    output_file.write_text(output, encoding="utf-8")
    print(f"\nDone. Output saved to: {output_file}", file=sys.stderr)
    print(f"  {len(merged)} sections merged.", file=sys.stderr)
    print(f"  Redirections section moved to top.", file=sys.stderr)


if __name__ == "__main__":
    main()