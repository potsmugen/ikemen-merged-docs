#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge M.U.G.E.N 1.1 + Ikemen GO State Controllers.
"""

import sys
from pathlib import Path
from merge_lib import *


def main():
    print("=" * 60, file=sys.stderr)
    print("MERGED STATE CONTROLLERS", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    mugen_file = Path("sctrl_mugen11.md")
    if not mugen_file.exists():
        print(f"ERROR: {mugen_file} not found", file=sys.stderr)
        sys.exit(1)

    mugen_text = load_file(mugen_file)

    changed_url = "https://raw.githubusercontent.com/wiki/ikemen-engine/Ikemen-GO/State-controllers-(changed).md"
    new_url = "https://raw.githubusercontent.com/wiki/ikemen-engine/Ikemen-GO/State-controllers-(new).md"

    print("Fetching Ikemen GO (changed)...", file=sys.stderr)
    changed_text = fetch_raw_markdown(changed_url)

    print("Fetching Ikemen GO (new)...", file=sys.stderr)
    new_text = fetch_raw_markdown(new_url)

    # Parse – keep "New state controller features" as one block
    mugen = parse_sections(mugen_text, keep_blocks=[])
    changed = parse_sections(changed_text, keep_blocks=[])
    new = parse_sections(new_text, keep_blocks=["New state controller features"])

    # Tag sources
    mugen = tag_sections(mugen, "(old)", skip_names=["About controllers"])
    changed = tag_sections(changed, "(changed)", replace_words=["parameters", "triggers"])
    new = tag_sections(new, "(new)")

    # Skip the "New state controllers" title section (it's just a header)
    skip = {"New state controllers"}

    # Merge all sections
    merged = merge_sections([
        ("M.U.G.E.N 1.1", mugen),
        ("Ikemen GO (changed)", changed),
        ("Ikemen GO (new)", new),
    ])

    print(f"Merged {len(merged)} sections.", file=sys.stderr)

    # Output with "About" and "New features" placed right after the TOC
    output = output_merged(
        merged,
        "Merged State Controller Reference",
        sections_to_skip=skip,
        top_sections=["About controllers", "New state controller features"]
    )

    output_file = Path("docs/sctrl.md")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(output, encoding="utf-8")
    print(f"\nDone. Output saved to: {output_file}", file=sys.stderr)
    print(f"  {len(merged)} sections merged.", file=sys.stderr)


if __name__ == "__main__":
    main()