#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Merge M.U.G.E.N 1.1 + Ikemen GO Trigger Redirections.
"""

import sys
from pathlib import Path
import re
from merge_lib import *


def extract_section(sections: Dict[str, str], name: str) -> Optional[str]:
    """Return the content of a named section, or None if not found."""
    # Case‑insensitive pop
    for key in list(sections.keys()):
        if key.lower() == name.lower():
            return sections.pop(key)
    return None


def split_redirections(content: str, source_label: str = "") -> Dict[str, str]:
    """
    Split a block of redirections into individual entries.
    Recognises both '## Heading' and '**Heading**' as entry delimiters.
    Each entry becomes a separate section with its heading preserved.
    """
    entries = {}
    lines = content.splitlines()
    current_key = None
    current_lines = []

    for line in lines:
        heading_match = re.match(r'^(#{2,})\s+(.+)$', line) or re.match(r'^\*\*(.+?)\*\*', line)
        if heading_match:
            if current_key is not None:
                entries[current_key] = '\n'.join(current_lines).strip()
            if heading_match.group(1).startswith('#'):
                raw = heading_match.group(2).strip()
            else:
                raw = heading_match.group(1).strip()
            current_key = clean_heading(raw)
            if source_label:
                current_key = f"{current_key} ({source_label})"
            current_lines = [line]
        else:
            if current_key is not None:
                current_lines.append(line)

    if current_key is not None:
        entries[current_key] = '\n'.join(current_lines).strip()

    return entries


def main():
    print("=" * 60, file=sys.stderr)
    print("MERGED REDIRECTIONS", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    # ------------------------------------------------------------------
    # 1. M.U.G.E.N redirections
    # ------------------------------------------------------------------

    mugen_file = Path("redirections_mugen11.md")

    if not mugen_file.exists():
        print(f"ERROR: {mugen_file} not found", file=sys.stderr)
        sys.exit(1)

    mugen_text = load_file(mugen_file)

    lines = mugen_text.splitlines()

    if lines and lines[0].startswith('# '):
        lines = lines[1:]

    mugen_content = '\n'.join(lines).strip()

    mugen_entries = split_redirections(
        mugen_content,
        source_label="M.U.G.E.N"
    )

    # ------------------------------------------------------------------
    # 2. Ikemen GO (changed) – using parse_sections
    # ------------------------------------------------------------------

    changed_url = (
        "https://raw.githubusercontent.com/wiki/ikemen-engine/Ikemen-GO/Triggers-(changed).md"
    )

    changed_text = fetch_raw_markdown(changed_url)

    # Parse the entire changed page into sections (special case prevents H2 splitting)
    changed_sections = parse_sections(changed_text)

    # Extract the "Changed trigger redirections" block (case‑insensitive)
    changed_redir_block = extract_section(
        changed_sections,
        "Changed trigger redirections"
    )

    if changed_redir_block:
        # Split the block into individual entries (handles ##, ###, bold, etc.)
        changed_entries = split_redirections(changed_redir_block)

        # Add source label
        changed_entries = {
            f"{name} (changed)": content
            for name, content in changed_entries.items()
        }
    else:
        changed_entries = {}

    print(
        f"Changed entries found: {list(changed_entries.keys())}",
        file=sys.stderr
    )

    # ------------------------------------------------------------------
    # 3. Ikemen GO (new)
    # ------------------------------------------------------------------

    new_url = (
        "https://raw.githubusercontent.com/wiki/ikemen-engine/Ikemen-GO/Triggers-(new).md"
    )

    new_text = fetch_raw_markdown(new_url)

    new_sections = parse_sections(new_text)

    new_redir_block = extract_section(
        new_sections,
        "New trigger redirections"
    )

    if new_redir_block:
        new_entries = split_redirections(
            new_redir_block,
            source_label="new"
        )
    else:
        new_entries = {}

    print(
        f"New entries found: {list(new_entries.keys())}",
        file=sys.stderr
    )

    # ------------------------------------------------------------------
    # Merge
    # ------------------------------------------------------------------

    sources = []

    if mugen_entries:
        sources.append(("M.U.G.E.N 1.1", mugen_entries))

    if changed_entries:
        sources.append(("Ikemen GO (changed)", changed_entries))

    if new_entries:
        sources.append(("Ikemen GO (new)", new_entries))

    merged = merge_sections(sources)

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    output = output_merged(
        merged,
        "Merged Trigger Redirection Reference",
        sections_to_skip=[],
        top_sections=[]
    )

    output_file = Path("docs/redirections.md")
    output_file.write_text(output, encoding="utf-8")

    print(
        f"\nDone. Output saved to: {output_file}",
        file=sys.stderr
    )

    print(
        f"  {len(merged)} redirection entries merged.",
        file=sys.stderr
    )

    print(
        f"  Changed entries: {len(changed_entries)}",
        file=sys.stderr
    )

    print(
        f"  New entries: {len(new_entries)}",
        file=sys.stderr
    )


if __name__ == "__main__":
    main()