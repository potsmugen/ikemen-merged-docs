#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared library for merging M.U.G.E.N + Ikemen GO documentation.
"""

import html
import re
import sys
from pathlib import Path
from typing import Dict, Set, Optional, List, Tuple
from urllib.parse import unquote, urlsplit, urlunsplit

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


def _section_body(content: str) -> str:
    return re.sub(r"^#{1,6}\s+[^\n]*(?:\n|$)", "", content, count=1).strip()


def require_sections(
    sections: Dict[str, str], required: List[str], source_name: str
) -> None:
    """Fail clearly when a source document no longer has expected sections."""
    if not sections:
        raise ValueError(f"{source_name} produced no sections")

    missing = [name for name in required if name not in sections]
    if missing:
        raise ValueError(
            f"{source_name} is missing required section(s): {', '.join(missing)}"
        )

    empty = [name for name in required if not _section_body(sections[name])]
    if empty:
        raise ValueError(
            f"{source_name} has empty required section(s): {', '.join(empty)}"
        )

    if not any(_section_body(content) for content in sections.values()):
        raise ValueError(f"{source_name} produced no documented sections")


def require_entries(entries: Dict[str, str], source_name: str) -> None:
    """Fail clearly when a parsed reference source has no documented entries."""
    if any(_section_body(content) for content in entries.values()):
        return
    raise ValueError(f"{source_name} produced no documented entries")


# ----------------------------------------------------------------------
# CODE BLOCK HIDING
# ----------------------------------------------------------------------

def hide_code_blocks(text: str) -> Tuple[str, Dict[str, str]]:
    """Replace fenced/indented code blocks with placeholders."""
    lines = text.splitlines()
    result = []
    placeholders = {}
    count = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            fence = '```' if stripped.startswith('```') else '~~~'
            placeholder = f"__CODE_BLOCK_{count}__"
            count += 1
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
        if line.startswith(('    ', '\t')):
            prev_blank = (not result) or (result[-1].strip() == '')
            if prev_blank:
                placeholder = f"__CODE_BLOCK_{count}__"
                count += 1
                block_lines = [line]
                i += 1
                while i < len(lines) and (lines[i].startswith(('    ', '\t')) or lines[i].strip() == ''):
                    block_lines.append(lines[i])
                    i += 1
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
    return pattern.sub(lambda m: placeholders.get(m.group(0), m.group(0)), text)


# ----------------------------------------------------------------------
# CLEAN HEADING
# ----------------------------------------------------------------------

def clean_heading(text: str) -> str:
    """Remove HTML tags and (nightly build only) from heading."""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s*\(nightly build only\)\s*', '', text, flags=re.IGNORECASE)
    return text.strip()


# ----------------------------------------------------------------------
# PARSE SECTIONS (unified)
# ----------------------------------------------------------------------

def parse_sections(text: str, split_level: int = 2, keep_blocks: List[str] = None) -> Dict[str, str]:
    """
    Split document into sections by headings of the given level (default ##).
    If keep_blocks is provided, those H1 sections are NOT split (they remain as one block).
    Code blocks are hidden during parsing.
    """
    if keep_blocks is None:
        keep_blocks = []
    processed, placeholders = hide_code_blocks(text)
    sections = {}
    lines = processed.splitlines()
    current_heading = None
    current_content = []
    in_keep_block = False

    for line in lines:
        # Detect H1
        m_h1 = re.match(r'^(#{1})\s+(.*)$', line)
        if m_h1:
            if current_heading is not None:
                sections[current_heading] = '\n'.join(current_content).strip()
            raw = m_h1.group(2).strip()
            heading = clean_heading(raw)
            current_heading = heading
            current_content = [line]
            in_keep_block = heading in keep_blocks
            continue

        # If not in a keep-block, split on the specified level
        if not in_keep_block:
            m = re.match(r'^(#{' + str(split_level) + r'})\s+(.*)$', line)
            if m:
                if current_heading is not None:
                    sections[current_heading] = '\n'.join(current_content).strip()
                raw = m.group(2).strip()
                heading = clean_heading(raw)
                current_heading = heading
                current_content = [line]
                continue

        if current_heading is not None:
            current_content.append(line)

    if current_heading is not None:
        sections[current_heading] = '\n'.join(current_content).strip()

    # Restore code blocks
    for k, v in sections.items():
        sections[k] = restore_code_blocks(v, placeholders)
    return sections


# ----------------------------------------------------------------------
# MERGE
# ----------------------------------------------------------------------

def merge_sections(sections_list: List[Tuple[str, Dict[str, str]]]) -> Dict[str, Dict[str, Set[str]]]:
    merged = {}
    for source_name, sections in sections_list:
        for heading, content in sections.items():
            lines = content.splitlines()
            heading_level = 2
            body_lines = lines
            if lines and re.match(r'^#{1,6}\s+', lines[0]):
                match = re.match(r'^(#{1,6})\s+', lines[0])
                heading_level = len(match.group(1))
                body_lines = lines[1:]
            body = '\n'.join(body_lines).strip()
            anchors = set()
            if lines:
                anchors = {
                    match.group(1)
                    for match in re.finditer(
                        r'<a\b[^>]*\b(?:name|id)\s*=\s*["\']([^"\']+)["\'][^>]*>',
                        lines[0],
                        re.IGNORECASE,
                    )
                }
            if heading in merged:
                merged[heading]['content'] += '\n\n' + body
                merged[heading]['sources'].add(source_name)
                merged[heading]['anchors'].update(anchors)
                merged[heading]['level'] = min(merged[heading]['level'], heading_level)
            else:
                merged[heading] = {
                    'content': body,
                    'sources': {source_name},
                    'level': heading_level,
                    'anchors': anchors,
                }
    return merged


# ----------------------------------------------------------------------
# TAG SECTIONS (generic)
# ----------------------------------------------------------------------

def tag_first_heading(content: str, suffix: str) -> str:
    """Tag only the first heading in the content block."""
    lines = content.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level, raw_text = m.group(1), m.group(2).strip()
            text = clean_heading(raw_text)
            if not re.search(rf'{re.escape(suffix)}$', text):
                text = f"{text} {suffix}"
            anchor = re.search(r'<a\b([^>]*)>(.*?)</a>', raw_text, re.IGNORECASE)
            if anchor:
                text = f"<a{anchor.group(1)}>{text}</a>"
            lines[i] = f"{level} {text}"
            break
    return '\n'.join(lines)


def tag_sections(
    sections: Dict[str, str],
    suffix: str,
    skip_names: List[str] = None,
    replace_words: List[str] = None
) -> Dict[str, str]:
    """
    Generic tagging:
    - If heading contains a word from replace_words, replace it with suffix.
    - Otherwise, append suffix.
    - Tags only the first heading in the content.
    - skip_names: headings to leave unchanged.
    """
    if skip_names is None:
        skip_names = []
    if replace_words is None:
        replace_words = ["parameters", "triggers"]

    tagged = {}
    for name, content in sections.items():
        # Skip if in skip list or already tagged
        if name in skip_names or re.search(r'\((old|changed|new)\)$', name):
            tagged[name] = content
            continue

        # Determine new name
        new_name = name
        if any(re.search(rf'\b{re.escape(w)}\b', name, re.IGNORECASE) for w in replace_words):
            # Replace the first matched word with suffix
            for w in replace_words:
                if re.search(rf'\b{re.escape(w)}\b', name, re.IGNORECASE):
                    new_name = re.sub(rf'(?i)\b{re.escape(w)}\b', suffix, name)
                    break
        else:
            new_name = f"{name} {suffix}"

        # Clean up spacing
        new_name = re.sub(r'\s+', ' ', new_name).strip()

        # Tag the first heading in content
        content = tag_first_heading(content, suffix)

        tagged[new_name] = content

    return tagged


# ----------------------------------------------------------------------
# LINK REWRITING
# ----------------------------------------------------------------------

def rewrite_links(text: str) -> str:
    """Route Ikemen wiki links to generated pages or the upstream wiki."""
    page_map = {
        "triggers": "triggers",
        "triggers-(changed)": "triggers",
        "triggers-(new)": "triggers",
        "state-controllers": "sctrl",
        "state-controllers-(changed)": "sctrl",
        "state-controllers-(new)": "sctrl",
    }
    anchor_aliases = {
        ("state-controllers-(new)", "new_gethitvarset"): "new_grthitvarset",
    }
    external_anchor_links = {
        # This upstream reference points to an anchor absent from the changed page.
        ("state-controllers-(changed)", "changed_projectile_platformangle"),
    }
    redirect_anchors = {
        "triggers": {
            "enemy": "enemy-old",
            "enemy_n": "enemyn-old",
            "enemy_near": "enemynear-old",
            "enemynear": "enemynear-old",
            "helper": "helper-old",
            "helper_id": "helperid-old",
            "parent": "parent-old",
            "partner": "partner-old",
            "partner_n": "partnern-old",
            "playerid": "playeridid-old",
            "root": "root-old",
            "target": "target-old",
            "target_id": "targetid-old",
        },
        "triggers-(changed)": {
            "helper": "helper-changed",
            "target": "target-changed",
        },
        "triggers-(new)": {
            "helperindex": "helperindexn-new",
            "p2": "p2-new",
            "player": "playern-new",
            "playerindex": "playerindexn-new",
            "stateowner": "stateowner-new",
        },
    }

    def rewrite(match):
        link_text = match.group(1)
        url = match.group(2)
        parsed = urlsplit(url)

        # Leave absolute URLs and same-page anchors unchanged.
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)

        # Relative paths to files (usually images) are not wiki page links.
        if Path(unquote(parsed.path)).suffix:
            return match.group(0)

        page = unquote(parsed.path).rstrip("/")
        while page.startswith("../"):
            page = page[3:]
        if page.startswith("./"):
            page = page[2:]
        page = page.lstrip("/")

        page_key = page.casefold()
        anchor = unquote(parsed.fragment)
        target = page_map.get(page_key)
        if (page_key, anchor.casefold()) in external_anchor_links:
            target = None
        if target:
            anchor = anchor_aliases.get((page_key, anchor.casefold()), anchor)
            redirect = re.match(r"^redirection[_-](.+)$", anchor, re.IGNORECASE)
            if redirect:
                anchor_name = redirect.group(1).casefold()
                anchor = redirect_anchors.get(page_key, {}).get(
                    anchor_name, slugify(anchor_name.replace("_", " "))
                )
                target = "redirections"
            rewritten = urlunsplit(("", "", target, parsed.query, anchor))
        else:
            wiki_path = page.replace(" ", "-")
            rewritten = urlunsplit(("https", "github.com", "/ikemen-engine/Ikemen-GO/wiki/" + wiki_path, parsed.query, parsed.fragment))

        return f"[{link_text}]({rewritten})"

    return re.sub(r'\[([^\]]+)\]\(((?:[^()]|\([^()]*\))+)\)', rewrite, text)


# ----------------------------------------------------------------------
# SLUG / SORT / TOC
# ----------------------------------------------------------------------

def slugify(text: str) -> str:
    slug = text.lower().replace(' ', '-')
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug or f"section-{hash(text) % 1000000}"


def get_sort_key(name: str) -> tuple:
    tag_match = re.search(r'\((old|changed|new)\)$', name)
    if tag_match:
        tag = tag_match.group(1)
        base = re.sub(r'\s*\((old|changed|new)\)$', '', name).strip()
        priority = {'old': 0, 'changed': 1, 'new': 2}.get(tag, 99)
    else:
        base, priority = name, 99
    return (base.lower(), priority)


def generate_toc_from_sections(merged: Dict[str, Dict[str, Set[str]]], sections_to_skip: List[str] = None) -> str:
    if sections_to_skip is None:
        sections_to_skip = []
    items = []
    for name in sorted(merged.keys(), key=get_sort_key):
        if name in sections_to_skip:
            continue
        clean = clean_heading(name)
        if clean:
            items.append(f"- [{clean}](#{slugify(clean)})")
    return "\n".join(items)


def strip_source_tag(name: str) -> str:
    """Remove any trailing (old), (changed), or (new) suffix."""
    return re.sub(r'\s*\((old|changed|new)\)$', '', name).strip()


# ----------------------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------------------

def output_merged(
    merged: Dict[str, Dict[str, Set[str]]],
    title: str,
    sections_to_skip: List[str] = None,
    top_sections: List[str] = None,
    list_heading: str = "# Main List"
) -> str:
    """
    Output the merged documentation with:
    - Table of contents (first)
    - Top sections (moved after TOC, headings kept)
    - A heading before the alphabetical list (customizable via list_heading)
    """
    if sections_to_skip is None:
        sections_to_skip = []
    if top_sections is None:
        top_sections = []

    lines = [f"# {title}", ""]

    # Find top sections (tag‑insensitive)
    top_keys = {}
    for top in top_sections:
        for k in merged.keys():
            if strip_source_tag(k).lower() == top.lower():
                top_keys[top] = k
                break

    # TOC (skip top sections)
    toc_skip = list(set(sections_to_skip) | set(top_keys.values()))
    toc = generate_toc_from_sections(merged, toc_skip)
    if toc:
        lines.extend(["## Table of Contents", "", toc, "", "---", ""])

    # Output top sections in requested order
    for top in top_sections:
        key = top_keys.get(top)
        if key and key in merged:
            data = merged.pop(key)
            content = data['content']
            level = data.get('level', 2)
            clean = clean_heading(key)
            lines.extend(
                f'<a id="{html.escape(anchor, quote=True)}"></a>'
                for anchor in sorted(data.get('anchors', set()))
            )
            lines.append(f"{'#' * level} {clean}")
            lines.append("")
            if content.strip():
                lines.append(content)
                lines.append("")
            lines.append("---")
            lines.append("")

    # Remaining sections with heading before list
    remaining = [n for n in merged.keys() if n not in sections_to_skip and merged[n]['content'].strip()]
    if remaining:
        lines.append(list_heading)
        lines.append("")

    for name in sorted(merged.keys(), key=get_sort_key):
        if name in sections_to_skip or not merged[name]['content'].strip():
            continue
        data = merged[name]
        content = data['content']
        level = data.get('level', 2)
        clean = clean_heading(name)
        lines.extend(
            f'<a id="{html.escape(anchor, quote=True)}"></a>'
            for anchor in sorted(data.get('anchors', set()))
        )
        lines.append(f"{'#' * level} {clean}")
        lines.append("")
        if content.strip():
            lines.append(content)
            lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)