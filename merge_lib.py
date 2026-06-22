#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared library for merging M.U.G.E.N + Ikemen GO documentation.
"""

import re
import sys
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
        # Only consider it a code block if it's preceded by a blank line or start of file
        if (line.startswith('    ') or line.startswith('\t')):
            prev_line_is_blank = (not result) or (result[-1].strip() == '')
            if prev_line_is_blank:
                placeholder = f"__CODE_BLOCK_{placeholder_count}__"
                placeholder_count += 1
                block_lines = [line]
                i += 1
                while i < len(lines):
                    if lines[i].startswith('    ') or lines[i].startswith('\t') or lines[i].strip() == '':
                        if lines[i].strip() == '':
                            j = i + 1
                            while j < len(lines) and lines[j].strip() == '':
                                j += 1
                            if j < len(lines) and (lines[j].startswith('    ') or lines[j].startswith('\t')):
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
    """Restore code blocks from placeholders."""
    if not placeholders:
        return text
    pattern = re.compile(r'__CODE_BLOCK_\d+__')

    def replacer(match):
        return placeholders.get(match.group(0), match.group(0))

    return pattern.sub(replacer, text)


# ----------------------------------------------------------------------
# CLEAN HEADING
# ----------------------------------------------------------------------

def clean_heading(text: str) -> str:
    """Remove HTML tags from heading text."""
    return re.sub(r'<[^>]+>', '', text).strip()


# ----------------------------------------------------------------------
# PARSE SECTIONS
# ----------------------------------------------------------------------

def parse_sections(text: str) -> Dict[str, str]:
    """
    Parse sections by ## headings. Code blocks are hidden during parsing.
    Special case: certain H1 sections keep all content as one block to avoid splitting.
    """
    processed, placeholders = hide_code_blocks(text)

    sections = {}
    lines = processed.splitlines()
    current_heading = None
    current_content = []
    in_special_section = False

    for line in lines:
        match_h1 = re.match(r'^(#{1})\s+(.*)$', line)
        if match_h1:
            if current_heading is not None:
                sections[current_heading] = '\n'.join(current_content).strip()
            raw_heading = match_h1.group(2).strip()
            heading = clean_heading(raw_heading)
            current_heading = heading
            current_content = [line]

            # These sections should be treated as a single block and not split by H2
            in_special_section = (heading == "New state controller features" or
                                  heading == "Universal state controller features" or
                                  heading == "New triggers" or
                                  heading == "New trigger redirections")
            continue

        if not in_special_section:
            match_h2 = re.match(r'^(#{2})\s+(.*)$', line)
            if match_h2:
                if current_heading is not None:
                    sections[current_heading] = '\n'.join(current_content).strip()
                raw_heading = match_h2.group(2).strip()
                heading = clean_heading(raw_heading)
                current_heading = heading
                current_content = [line]
                continue

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
    """
    Merge sections from multiple sources with source tracking.
    When merging, separate the heading from the body to prevent tag bleeding.
    """
    merged = {}
    for source_name, sections in sections_list:
        for heading, content in sections.items():
            # Separate the heading from the body
            lines = content.splitlines()
            heading_level = 2  # default
            body_lines = lines

            if lines and re.match(r'^#{1,6}\s+', lines[0]):
                match = re.match(r'^(#{1,6})\s+', lines[0])
                heading_level = len(match.group(1))
                body_lines = lines[1:]

            body = '\n'.join(body_lines).strip()

            if heading in merged:
                merged[heading]['content'] += '\n\n' + body
                merged[heading]['sources'].add(source_name)
                # Use the minimum heading level (highest priority)
                merged[heading]['level'] = min(merged[heading]['level'], heading_level)
            else:
                merged[heading] = {
                    'content': body,
                    'sources': {source_name},
                    'level': heading_level
                }
    return merged


def source_tag_str(sources: Set[str]) -> str:
    """Format source tags as a pipe-separated string."""
    return " | ".join(sorted(sources))


# ----------------------------------------------------------------------
# RENAME CHANGED SECTIONS
# ----------------------------------------------------------------------

def rename_changed_sections(sections: Dict[str, str], suffix: str = "(changed)") -> Dict[str, str]:
    """
    Replace 'parameters' or 'triggers' with suffix in headings from the changed page.
    Also updates the heading line inside the content.
    """
    renamed = {}
    for name, content in sections.items():
        # Skip special sections
        if name in ("New state controller features", "New trigger redirections"):
            renamed[name] = content
            continue

        # Check for both parameters and triggers
        if "parameters" in name.lower() or "triggers" in name.lower():
            new_name = re.sub(r'(?i)\s*(parameters|triggers)\s*', f' {suffix} ', name).strip()
            new_name = re.sub(r'\s+', ' ', new_name).strip()
            renamed[new_name] = content

            # Also update the heading inside the content
            content_lines = content.splitlines()
            if content_lines and re.match(r'^#{1,6}\s+', content_lines[0]):
                heading_text = re.sub(r'^#{1,6}\s+', '', content_lines[0])
                new_heading_text = re.sub(r'(?i)\s*(parameters|triggers)\s*', f' {suffix} ', heading_text).strip()
                new_heading_text = re.sub(r'\s+', ' ', new_heading_text).strip()
                content_lines[0] = f"## {new_heading_text}"
                renamed[new_name] = '\n'.join(content_lines)
        else:
            renamed[name] = content

    return renamed


# ----------------------------------------------------------------------
# SLUG GENERATION (GitHub-compatible)
# ----------------------------------------------------------------------

def slugify(text: str) -> str:
    """
    Generate a GitHub-style anchor slug from a heading.
    Converts to lowercase, replaces spaces with hyphens,
    removes non-alphanumeric characters (except hyphens).
    """
    # Lowercase
    slug = text.lower()
    # Replace spaces with hyphens
    slug = slug.replace(' ', '-')
    # Remove any character that is not alphanumeric or hyphen
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # Collapse multiple hyphens
    slug = re.sub(r'-+', '-', slug)
    # Strip leading/trailing hyphens
    slug = slug.strip('-')
    # If empty, use a fallback
    if not slug:
        slug = f"section-{hash(text) % 1000000}"
    return slug


# ----------------------------------------------------------------------
# TOC GENERATION (Simple Markdown List)
# ----------------------------------------------------------------------

def generate_toc_from_sections(merged: Dict[str, Dict[str, Set[str]]], sections_to_skip: List[str] = None) -> str:
    """
    Generate a table of contents from section headings.
    Uses slugify for robust anchor links.
    """
    if sections_to_skip is None:
        sections_to_skip = []

    items = []
    for name in sorted(merged.keys(), key=lambda s: s.lower()):
        if name in sections_to_skip:
            continue

        # Clean the name (remove any HTML tags)
        clean_name = clean_heading(name)
        if not clean_name:
            continue

        # Generate slug
        slug = slugify(clean_name)

        items.append(f"- [{clean_name}](#{slug})")

    return "\n".join(items) if items else ""


# ----------------------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------------------

def output_merged(
    merged: Dict[str, Dict[str, Set[str]]],
    title: str,
    sections_to_skip: List[str] = None
) -> str:
    """
    Output the merged documentation with:
    - Table of contents (first)
    - Universal section
    - Alphabetical listing with source tags
    """
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

    lines = [style, "", f"# {title}", ""]

    # --- Generate TOC from ALL sections (including universal) ---
    toc = generate_toc_from_sections(merged, sections_to_skip)
    if toc:
        lines.append("## Table of Contents")
        lines.append("")
        lines.append(toc)
        lines.append("")
        lines.append("---")
        lines.append("")

    # --- Extract Universal section if present ---
    # The Universal section comes from the "new" page and contains global features like RedirectID
    universal_key = None
    for key in merged.keys():
        if key in ("New state controller features", "Universal state controller features"):
            universal_key = key
            break

    if universal_key:
        universal_data = merged.pop(universal_key)
        universal_content = universal_data['content']
        universal_level = universal_data.get('level', 1)

        # Clean tags
        universal_content = re.sub(r'<a[^>]+>', '', universal_content)
        universal_content = re.sub(r'</a>', '', universal_content)

        # Ensure the heading is correct
        clean_universal = clean_heading(universal_key)
        lines.append(f"{'#' * universal_level} {clean_universal}")
        lines.append("")
        if universal_content.strip():
            lines.append(universal_content)
            lines.append("")
        lines.append("---")
        lines.append("")

    # --- Output remaining sections alphabetically ---
    for name in sorted(merged.keys(), key=lambda s: s.lower()):
        if name in sections_to_skip:
            continue
        if not merged[name]['content'].strip():
            continue

        data = merged[name]
        content = data['content']
        sources = source_tag_str(data['sources'])
        level = data.get('level', 2)

        # Clean the name and content
        clean_name = clean_heading(name)
        content = re.sub(r'<a[^>]+>', '', content)
        content = re.sub(r'</a>', '', content)

        lines.append(f"{'#' * level} {clean_name}")
        lines.append("")
        lines.append(f"*Source: {sources}*")
        lines.append("")
        if content.strip():
            lines.append(content)
            lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)