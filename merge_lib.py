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
    """Remove HTML tags and suffixes like (nightly build only) from heading text."""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s*\(nightly build only\)\s*', '', text, flags=re.IGNORECASE)
    return text.strip()


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
                                  heading == "New triggers" or
                                  heading == "New trigger redirections" or
                                  heading == "Changed trigger redirections")
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
# PARSE SUB-SECTIONS
# ----------------------------------------------------------------------

def parse_sub_sections(text: str) -> Dict[str, str]:
    """
    Parse a block of text into sub-sections by ## headings.
    Used for extracting individual triggers from the "New triggers" block.
    """
    sections = {}
    lines = text.splitlines()
    current_heading = None
    current_content = []

    for line in lines:
        match = re.match(r'^(#{2})\s+(.*)$', line)
        if match:
            if current_heading is not None:
                sections[current_heading] = '\n'.join(current_content).strip()
            raw_heading = match.group(2).strip()
            heading = clean_heading(raw_heading)
            current_heading = heading
            current_content = [line]
        else:
            if current_heading is not None:
                current_content.append(line)

    if current_heading is not None:
        sections[current_heading] = '\n'.join(current_content).strip()

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
                merged[heading]['level'] = min(merged[heading]['level'], heading_level)
            else:
                merged[heading] = {
                    'content': body,
                    'sources': {source_name},
                    'level': heading_level
                }
    return merged


def source_tag_str(sources: Set[str]) -> str:
    """Format source tags as a comma-separated string."""
    return ", ".join(sorted(sources))


# ----------------------------------------------------------------------
# HELPER TO TAG THE FIRST HEADING ONLY
# ----------------------------------------------------------------------

def tag_first_heading(content: str, suffix: str) -> str:
    """
    Tag only the first heading in the content (any level: H1-H6).
    Leaves all other headings untouched.
    """
    lines = content.splitlines()
    if not lines:
        return content

    # Find the first line that contains a heading
    for i, line in enumerate(lines):
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = m.group(1)
            heading_text = m.group(2).strip()
            heading_text = clean_heading(heading_text)
            if not re.search(rf'{re.escape(suffix)}$', heading_text):
                heading_text = f"{heading_text} {suffix}"
            lines[i] = f"{level} {heading_text}"
            break

    return '\n'.join(lines)


# ----------------------------------------------------------------------
# RENAME CHANGED SECTIONS
# ----------------------------------------------------------------------

def rename_changed_sections(sections: Dict[str, str], suffix: str = "(changed)") -> Dict[str, str]:
    """
    Rename sections from the changed page:
    - For any section, tag the first heading (block header) and the dict key.
    - Leaves all other headings inside the block untouched.
    """
    renamed = {}
    tag_word = suffix.strip('()')  # "changed"
    for name, content in sections.items():
        # If name already contains the tag word, keep it as-is
        if re.search(rf'\b{re.escape(tag_word)}\b', name, re.IGNORECASE):
            renamed[name] = content
            continue

        # Determine new heading name
        if re.search(r'(?i)\b(parameters|triggers)\b', name):
            new_name = re.sub(r'(?i)\s*(parameters|triggers)\s*', f' {suffix} ', name).strip()
            new_name = re.sub(r'\s+', ' ', new_name).strip()
        else:
            new_name = f"{name} {suffix}"

        # Tag only the first heading inside the content
        content = tag_first_heading(content, suffix)

        renamed[new_name] = content

    return renamed


# ----------------------------------------------------------------------
# TAG OLD AND NEW SECTIONS
# ----------------------------------------------------------------------

def tag_old_sections(sections: Dict[str, str], suffix: str = "(old)") -> Dict[str, str]:
    """
    Tag M.U.G.E.N sections with (old) suffix.
    Tags the first heading (block header) and the dict key.
    Leaves all other headings inside the block untouched.
    Skips "About controllers" to keep it untagged.
    """
    tagged = {}
    for name, content in sections.items():
        # Skip "About controllers" and other special sections that we want to keep as-is
        if name in ("About controllers", "New trigger redirections", "Changed trigger redirections", "New triggers"):
            tagged[name] = content
            continue

        # If already has a suffix, keep
        if re.search(r'\((old|changed|new)\)$', name):
            tagged[name] = content
            continue

        new_name = f"{name} {suffix}"
        # Tag only the first heading inside the content
        content = tag_first_heading(content, suffix)

        tagged[new_name] = content

    return tagged


def tag_new_sections(sections: Dict[str, str], suffix: str = "(new)") -> Dict[str, str]:
    """
    Tag Ikemen GO new sections with (new) suffix.
    Tags the first heading (block header) and the dict key.
    Leaves all other headings inside the block untouched.
    Skips redirection sections.
    """
    tagged = {}
    for name, content in sections.items():
        # Skip redirection sections entirely
        if name in ("New trigger redirections", "Changed trigger redirections"):
            tagged[name] = content
            continue

        # If already has a suffix, keep
        if re.search(r'\((old|changed|new)\)$', name):
            tagged[name] = content
            continue

        new_name = f"{name} {suffix}"
        # Tag only the first heading inside the content
        content = tag_first_heading(content, suffix)

        tagged[new_name] = content

    return tagged


# ----------------------------------------------------------------------
# SLUG GENERATION (GitHub-compatible)
# ----------------------------------------------------------------------

def slugify(text: str) -> str:
    """
    Generate a GitHub-style anchor slug from a heading.
    Converts to lowercase, replaces spaces with hyphens,
    removes non-alphanumeric characters (except hyphens).
    """
    slug = text.lower()
    slug = slug.replace(' ', '-')
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')
    if not slug:
        slug = f"section-{hash(text) % 1000000}"
    return slug


# ----------------------------------------------------------------------
# SORT KEY HELPERS
# ----------------------------------------------------------------------

def get_sort_key(name: str) -> tuple:
    """
    Sort key for sections: primary = base name (without tag),
    secondary = tag priority (old=0, changed=1, new=2).
    Sections without a tag come after all tagged ones.
    """
    tag_match = re.search(r'\((old|changed|new)\)$', name)
    if tag_match:
        tag = tag_match.group(1)
        base_name = re.sub(r'\s*\((old|changed|new)\)$', '', name).strip()
        tag_priority = {'old': 0, 'changed': 1, 'new': 2}.get(tag, 99)
    else:
        base_name = name
        tag_priority = 99
    return (base_name.lower(), tag_priority)


# ----------------------------------------------------------------------
# TOC GENERATION (Simple Markdown List)
# ----------------------------------------------------------------------

def generate_toc_from_sections(merged: Dict[str, Dict[str, Set[str]]], sections_to_skip: List[str] = None) -> str:
    """
    Generate a table of contents from section headings.
    Uses slugify for robust anchor links.
    Sorted by base name, then tag priority.
    """
    if sections_to_skip is None:
        sections_to_skip = []

    items = []
    for name in sorted(merged.keys(), key=get_sort_key):
        if name in sections_to_skip:
            continue
        clean_name = clean_heading(name)
        if not clean_name:
            continue
        slug = slugify(clean_name)
        items.append(f"- [{clean_name}](#{slug})")

    return "\n".join(items) if items else ""


# ----------------------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------------------

def strip_source_tag(name: str) -> str:
    """Remove any trailing (old), (changed), or (new) suffix."""
    return re.sub(r'\s*\((old|changed|new)\)$', '', name).strip()


def output_merged(
    merged: Dict[str, Dict[str, Set[str]]],
    title: str,
    sections_to_skip: List[str] = None,
    top_sections: List[str] = None
) -> str:
    """
    Output the merged documentation with:
    - Table of contents (first)
    - Top sections (moved after TOC, headings kept)
    - A "# State Controller Reference" heading before the alphabetical list
    """
    if sections_to_skip is None:
        sections_to_skip = []
    if top_sections is None:
        top_sections = []

    lines = [f"# {title}", ""]

    # Helper to strip tag for matching
    def strip_source_tag(name: str) -> str:
        return re.sub(r'\s*\((old|changed|new)\)$', '', name).strip()

    # Identify top sections
    top_keys_to_move = {}
    for top_key in top_sections:
        for k in merged.keys():
            if strip_source_tag(k).lower() == top_key.lower():
                top_keys_to_move[top_key] = k
                break

    # Generate TOC
    skip_for_toc = list(set(sections_to_skip) | set(top_keys_to_move.values()))
    toc = generate_toc_from_sections(merged, skip_for_toc)
    if toc:
        lines.append("## Table of Contents")
        lines.append("")
        lines.append(toc)
        lines.append("")
        lines.append("---")
        lines.append("")

    # Output top sections
    for top_key in top_sections:
        actual_key = top_keys_to_move.get(top_key)
        if actual_key and actual_key in merged:
            top_data = merged.pop(actual_key)
            top_content = top_data['content']
            top_level = top_data.get('level', 2)

            top_content = re.sub(r'<a[^>]+>', '', top_content)
            top_content = re.sub(r'</a>', '', top_content)
            clean_top = clean_heading(actual_key)

            lines.append(f"{'#' * top_level} {clean_top}")
            lines.append("")
            if top_content.strip():
                lines.append(top_content)
                lines.append("")
            lines.append("---")
            lines.append("")

    # ---------------------------------------------------------
    # 4. Output remaining sections sorted by base name, then tag
    #    with a "# State Controller Reference" heading before the list
    # ---------------------------------------------------------
    remaining = [name for name in merged.keys() if name not in sections_to_skip and merged[name]['content'].strip()]
    if remaining:
        lines.append("# State Controller Reference")
        lines.append("")

    for name in sorted(merged.keys(), key=get_sort_key):
        if name in sections_to_skip:
            continue
        if not merged[name]['content'].strip():
            continue

        data = merged[name]
        content = data['content']
        level = data.get('level', 2)

        content = re.sub(r'<a[^>]+>', '', content)
        content = re.sub(r'</a>', '', content)

        clean_name = clean_heading(name)

        lines.append(f"{'#' * level} {clean_name}")
        lines.append("")
        if content.strip():
            lines.append(content)
            lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)