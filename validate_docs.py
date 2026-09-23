#!/usr/bin/env python3
"""Validate generated Pages documents before they are committed."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from merge_lib import hide_code_blocks, slugify


PAGES = {
    "sctrl.md": "State Controller Reference",
    "triggers.md": "Trigger Reference",
    "redirections.md": "Trigger Redirection Reference",
}
INTERNAL_ROUTES = {"sctrl", "triggers", "redirections"}
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(((?:[^()]|\([^()]*\))+)\)")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+.+$", re.MULTILINE)
ANCHOR_PATTERN = re.compile(
    r'<a\b[^>]*\b(?:id|name)\s*=\s*["\']([^"\']+)["\'][^>]*>',
    re.IGNORECASE,
)


def _anchor_ids(content: str) -> set[str]:
    anchors = set(ANCHOR_PATTERN.findall(content))
    for heading in HEADING_PATTERN.findall(content):
        text = re.sub(r"<[^>]+>", "", heading.split(None, 1)[1]).strip()
        anchors.add(slugify(text))
    return anchors


def validate_generated_docs(docs_dir: Path = Path("docs")) -> None:
    errors = []

    for filename, title in PAGES.items():
        path = docs_dir / filename
        if not path.is_file():
            errors.append(f"{path}: generated page is missing")
            continue

        content = path.read_text(encoding="utf-8")
        if not content.startswith(f"# {title}\n"):
            errors.append(f"{path}: expected title '# {title}'")
        if "## Table of Contents" not in content:
            errors.append(f"{path}: table of contents is missing")
        if len(HEADING_PATTERN.findall(content)) < 3:
            errors.append(f"{path}: too few headings; generated content may be incomplete")

        visible_content, _ = hide_code_blocks(content)
        for match in LINK_PATTERN.finditer(visible_content):
            destination = match.group(2).strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            if Path(parsed.path).suffix:
                continue

            route = parsed.path.rstrip("/").casefold()
            if route not in INTERNAL_ROUTES:
                errors.append(
                    f"{path}: unresolved relative page link '{destination}'"
                )
            elif not (docs_dir / f"{route}.md").is_file():
                errors.append(f"{path}: internal page link target '{route}' is missing")
            elif parsed.fragment:
                target_content = (docs_dir / f"{route}.md").read_text(encoding="utf-8")
                if unquote(parsed.fragment) not in _anchor_ids(target_content):
                    errors.append(
                        f"{path}: anchor '#{parsed.fragment}' is missing from '{route}'"
                    )

    if errors:
        raise ValueError("\n".join(errors))


def main() -> int:
    try:
        validate_generated_docs()
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    print("Generated documentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
