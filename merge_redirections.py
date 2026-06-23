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
    return sections.pop(name, None)


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


def extract_changed_redirections(raw_text: str) -> Dict[str, str]:
    """
    Extract the "Changed trigger redirections" section from the raw changed page.
    """
    lines = raw_text.splitlines()
    start_idx = None

    # Find the start of the section
    for i, line in enumerate(lines):
        if re.match(r'^\s*#\s+Changed trigger redirections', line):
            start_idx = i
            break

    if start_idx is None:
        print("DEBUG: Could not find '# Changed trigger redirections'", file=sys.stderr)
        return {}

    # Find the next top-level heading (starts with '# ') to end the section
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if re.match(r'^\s*#\s+', lines[i]):
            end_idx = i
            break

    print(f"DEBUG: start_idx={start_idx}, end_idx={end_idx}", file=sys.stderr)
    section_lines = lines[start_idx:end_idx]

    if not section_lines:
        print("DEBUG: section_lines is empty", file=sys.stderr)
        return {}

    print(f"DEBUG: First 5 lines of section:", file=sys.stderr)
    for i, line in enumerate(section_lines[:5]):
        print(f"  {i}: {repr(line)}", file=sys.stderr)

    # The first line may contain both the section heading and the first entry heading:
    # "# Changed trigger redirections ## Helper"
    first_line = section_lines[0]
    if '## ' in first_line:
        parts = first_line.split('## ', 1)
        section_lines[0] = "## " + parts[1].strip()
        print(f"DEBUG: Replaced first line with: {repr(section_lines[0])}", file=sys.stderr)
    else:
        print("DEBUG: No '## ' in first line", file=sys.stderr)

    # Now process the section lines to extract entries
    entries = {}
    current_key = None
    current_lines = []

    for line in section_lines:
        m = re.match(r'^\s*##\s+(.+)$', line)
        if m:
            if current_key is not None:
                entries[current_key] = '\n'.join(current_lines).strip()
            current_key = clean_heading(m.group(1).strip())
            current_lines = [line]
            print(f"DEBUG: Started new entry: {current_key}", file=sys.stderr)
        else:
            if current_key is not None:
                current_lines.append(line)

    if current_key is not None:
        entries[current_key] = '\n'.join(current_lines).strip()

    print(f"DEBUG: Found {len(entries)} entries", file=sys.stderr)
    return entries


def main():
    print("=" * 60, file=sys.stderr)
    print("MERGED REDIRECTIONS", file=sys.stderr)
    print("=" * 60, file=sys.stderr)

    # 1. M.U.G.E.N redirections
    mugen_file = Path("redirections_mugen11.md")
    if not mugen_file.exists():
        print(f"ERROR: {mugen_file} not found", file=sys.stderr)
        sys.exit(1)
    mugen_text = load_file(mugen_file)
    # Remove the H1 heading
    lines = mugen_text.splitlines()
    if lines and lines[0].startswith('# '):
        lines = lines[1:]
    mugen_content = '\n'.join(lines).strip()
    mugen_entries = split_redirections(mugen_content, source_label="M.U.G.E.N")

    # 2. Ikemen GO (changed)
    changed_url = "https://raw.githubusercontent.com/wiki/ikemen-engine/Ikemen-GO/Triggers-(changed).md"
    changed_text = fetch_raw_markdown(changed_url)
    changed_entries = extract_changed_redirections(changed_text)
    # Add source label to each entry
    changed_entries = {f"{k} (changed)": v for k, v in changed_entries.items()}

    # 3. Ikemen GO (new)
    new_url = "https://raw.githubusercontent.com/wiki/ikemen-engine/Ikemen-GO/Triggers-(new).md"
    new_text = fetch_raw_markdown(new_url)
    new_sections = parse_sections(new_text)
    new_redir_block = extract_section(new_sections, "New trigger redirections")
    if new_redir_block:
        new_entries = split_redirections(new_redir_block, source_label="new")
    else:
        new_entries = {}

    # Build source list for merge_sections
    sources = []
    if mugen_entries:
        sources.append(("M.U.G.E.N 1.1", mugen_entries))
    if changed_entries:
        sources.append(("Ikemen GO (changed)", changed_entries))
    if new_entries:
        sources.append(("Ikemen GO (new)", new_entries))

    merged = merge_sections(sources)

    # Output with TOC listing each redirection
    output = output_merged(
        merged,
        "Merged Trigger Redirection Reference",
        sections_to_skip=[],
        top_sections=[]
    )

    output_file = Path("docs/redirections.md")
    output_file.write_text(output, encoding="utf-8")
    print(f"\nDone. Output saved to: {output_file}", file=sys.stderr)
    print(f"  {len(merged)} redirection entries merged.", file=sys.stderr)
    print(f"  Changed entries: {len(changed_entries)}", file=sys.stderr)


if __name__ == "__main__":
    main()