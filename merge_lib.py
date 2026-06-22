#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared library for merging M.U.G.E.N + Ikemen GO documentation.
"""

import re
from pathlib import Path
from typing import Dict, Set, Optional, List, Tuple

try:
    import requests
except ImportError:
    print("Install: pip install requests", file=sys.stderr)
    sys.exit(1)


# ----------------------------------------------------------------------
# FETCH
# ----------------------------------------------------------------------

def fetch_raw_markdown(url: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, timeout=30, headers=headers)
    resp.raise_for_status()
    return resp.text


def load_file(filepath: Path) -> str:
    if not filepath.exists():
        return ""
    return filepath.read_text(encoding="utf-8").strip()


# ----------------------------------------------------------------------
# CODE BLOCK HIDING (ROBUST)
# ----------------------------------------------------------------------

def hide_code_blocks(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Replace every code block (fenced or indented) with a placeholder.
    Returns: (processed_text, {placeholder: original_block_content})
    """
    lines = text.splitlines()
    result = []
    placeholders = {}
    placeholder_count = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        # --- Fenced code block (``` or ~~~) ---
        if stripped.startswith('```') or stripped.startswith('~~~'):
            fence = '```' if stripped.startswith('```') else '~~~'
            placeholder = f"__CODE_BLOCK_{placeholder_count}__"
            placeholder_count += 1
            block_lines = [line]
            i += 1
            while i < len(lines):
                block_lines.append(lines[i])
                if lines[i].lstrip().startswith(fence):
                    i += 1
                    break
                i += 1
            placeholders[placeholder] = '\n'.join(block_lines)
            result.append(placeholder)
            continue

        # --- Indented code block (4 spaces or tab) ---
        if line.startswith('    ') or line.startswith('\t'):
            placeholder = f"__CODE_BLOCK_{placeholder_count}__"
            placeholder_count += 1
            block_lines = [line]
            i += 1
            while i < len(lines):
                if lines[i].startswith('    ') or lines[i].startswith('\t') \
                        or lines[i].strip() == '':
                    if lines[i].strip() == '':
                        j = i + 1
                        while j < len(lines) and lines[j].strip() == '':
                            j += 1
                        if j < len(lines) and \
                                (lines[j].startswith('    ') or lines[j].startswith('\t')):
                            block_lines.append(lines[i])
                            i += 1
                            continue
                        else:
                            break
                    block_lines.append(lines[i])
                    i += 1
                else:
                    break
            placeholders[placeholder] = '\n'.join(block_lines)
            result.append(placeholder)
            continue

        result.append(line)
        i += 1

    return '\n'.join(result), placeholders


def restore_code_blocks(text: str, placeholders: Dict[str, str]) -> str:
    if not placeholders:
        return text
    pattern = re.compile(r'__CODE_BLOCK_\d+__')

    def replacer(match):
        return placeholders.get(match.group(0), match.group(0))

    return pattern.sub(replacer, text)


# ----------------------------------------------------------------------
# PARSE SECTIONS
# ----------------------------------------------------------------------

def parse_sections(text: str) -> Dict[str, str]:
    """
    Parse sections by ## headings. Code blocks are hidden during parsing.
    Special case: 'New state controller features' section keeps all content as one block.
    """
    processed, placeholders = hide_code_blocks(text)

    sections = {}
    lines = processed.splitlines()
    current_heading = None
    current_content = []
    in_special_section = False

    for line in lines:
        # Check for # headings (level 1)
        match_h1 = re.match(r'^(#{1})\s+(.*)$', line)
        if match_h1:
            # Save previous section
            if current_heading is not None:
                sections[current_heading] = '\n'.join(current_content).strip()

            raw_heading = match_h1.group(2).strip()
            heading = re.sub(r'<[^>]+>', '', raw_heading).strip()
            current_heading = heading
            current_content = [line]
            # Check if this is a special section (should keep all content)
            in_special_section = (heading == "New state controller features" or 
                                   heading == "Universal state controller features")
            continue

        # Check for ## headings (level 2) – but NOT if we're in a special section
        if not in_special_section:
            match_h2 = re.match(r'^(#{2})\s+(.*)$', line)
            if match_h2:
                if current_heading is not None:
                    sections[current_heading] = '\n'.join(current_content).strip()
                raw_heading = match_h2.group(2).strip()
                heading = re.sub(r'<[^>]+>', '', raw_heading).strip()
                current_heading = heading
                current_content = [line]
                continue

        # All other lines: add to current content
        if current_heading is not None:
            current_content.append(line)

    if current_heading is not None:
        sections[current_heading] = '\n'.join(current_content).strip()

    for heading, content in sections.items():
        sections[heading] = restore_code_blocks(content, placeholders)

    return sections


# ----------------------------------------------------------------------
# MERGE WITH SOURCE TAGGING
# ----------------------------------------------------------------------

def merge_sections(sections_list: List[Tuple[str, Dict[str, str]]]) -> Dict[str, Dict[str, Set[str]]]:
    merged = {}
    for source_name, sections in sections_list:
        for heading, content in sections.items():
            if heading in merged:
                merged[heading]['content'] += '\n\n' + content
                merged[heading]['sources'].add(source_name)
            else:
                merged[heading] = {'content': content, 'sources': {source_name}}
    return merged


def source_tag_str(sources: Set[str]) -> str:
    return " | ".join(sorted(sources))


# ----------------------------------------------------------------------
# RENAME CHANGED SECTIONS
# ----------------------------------------------------------------------

def rename_changed_sections(sections: Dict[str, str], suffix: str = "(changed)") -> Dict[str, str]:
    """
    Replace 'parameters' or 'triggers' with suffix in headings from the changed page.
    """
    renamed = {}
    for name, content in sections.items():
        if name == "New state controller features" or name == "New trigger redirections":
            renamed[name] = content
            continue

        # Check for both parameters and triggers
        if "parameters" in name.lower() or "triggers" in name.lower():
            new_name = re.sub(r'(?i)\s*(parameters|triggers)\s*', f' {suffix} ', name).strip()
            new_name = re.sub(r'\s+', ' ', new_name).strip()
            renamed[new_name] = content

            # Also update the heading inside the content
            content_lines = content.splitlines()
            if content_lines and re.match(r'^##\s+', content_lines[0]):
                heading_text = re.sub(r'^##\s+', '', content_lines[0])
                new_heading_text = re.sub(r'(?i)\s*(parameters|triggers)\s*', f' {suffix} ', heading_text).strip()
                new_heading_text = re.sub(r'\s+', ' ', new_heading_text).strip()
                content_lines[0] = f"## {new_heading_text}"
                renamed[new_name] = '\n'.join(content_lines)
        else:
            renamed[name] = content

    return renamed


# ----------------------------------------------------------------------
# TOC GENERATION (Multi‑column)
# ----------------------------------------------------------------------

def generate_toc_from_sections(merged: Dict[str, Dict[str, Set[str]]], sections_to_skip: List[str] = None) -> str:
    """
    Generate a multi‑column table of contents from section headings.
    """
    if sections_to_skip is None:
        sections_to_skip = []

    items = []
    for name in sorted(merged.keys(), key=lambda s: s.lower()):
        if name in sections_to_skip:
            continue
        # Create slug: lowercase, spaces to hyphens, remove punctuation
        slug = name.lower().replace(" ", "-")
        slug = re.sub(r'[`()"\'\.]', '', slug)
        items.append(f'<li><a href="#{slug}">{name}</a></li>')

    if not items:
        return ""

    toc_html = f"""
    <div style="column-count: 2; column-gap: 2em;">
      <ul style="margin: 0; padding-left: 1.2em; list-style-type: disc;">
        {''.join(items)}
      </ul>
    </div>
    """
    return toc_html


# ----------------------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------------------

def output_merged(
    merged: Dict[str, Dict[str, Set[str]]],
    title: str,
    sections_to_skip: List[str] = None
) -> str:
    if sections_to_skip is None:
        sections_to_skip = []

    # Wide layout style
    style = """
    <style>
    .markdown-body {
      max-width: 1200px !important;
      margin: 0 auto !important;
      padding: 0 40px !important;
    }
    </style>
    """

    lines = [
        style,
        "",
        f"# {title}",
        "",
    ]

    # Generate TOC from remaining sections
    toc = generate_toc_from_sections(merged, sections_to_skip)
    if toc:
        lines.append("## Table of Contents")
        lines.append("")
        lines.append(toc)
        lines.append("")
        lines.append("---")
        lines.append("")

    for name in sorted(merged.keys(), key=lambda s: s.lower()):
        if name in sections_to_skip:
            continue
        if not merged[name]['content'].strip():
            print(f"WARNING: Empty content for section '{name}'", file=sys.stderr)
            continue

        data = merged[name]
        content = data['content']
        sources = source_tag_str(data['sources'])

        content = re.sub(r'<a[^>]+>', '', content)
        content = re.sub(r'</a>', '', content)

        content_lines = content.splitlines()
        heading_line = content_lines[0] if content_lines else ""
        rest_content = '\n'.join(content_lines[1:]) if len(content_lines) > 1 else ""

        lines.append(heading_line)
        lines.append("")
        lines.append(f"*Source: {sources}*")
        lines.append("")
        if rest_content.strip():
            lines.append(rest_content)
            lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)