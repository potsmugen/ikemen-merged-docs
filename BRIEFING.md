# Repository Briefing

## Purpose

This repository merges the Ikemen GO wiki with M.U.G.E.N 1.1 documentation. Ikemen GO supports all M.U.G.E.N features and adds more; all reference pages describe Ikemen GO behavior. The generated pages are hosted at <https://potsmugen.github.io/ikemen-merged-docs/>.

## Repository map

- `merge_lib.py` — shared Markdown parsing, section merging, link rewriting, and output generation.
- `merge_sctrl.py` — builds the state-controller reference.
- `merge_triggers.py` — builds the trigger reference.
- `merge_redirections.py` — builds the trigger-redirection reference.
- `static/` — checked-in M.U.G.E.N source Markdown and the landing-page template.
- `docs/` — GitHub Pages/Jekyll configuration, landing page, assets, and generated reference pages.
- `.github/workflows/update.yml` — scheduled generator workflow; installs Python dependencies, runs all three scripts, and commits changed docs.

Run the scripts from the repository root. They use relative paths, fetch current Ikemen GO wiki Markdown over HTTP, and write generated pages under `docs/`. `requests` is required.

## Scope and maintenance notes

This is a documentation merger, not an editorial spellchecker or style linter. Keep validation focused on merge integrity: expected source sections, generated pages, and links between pages. Do not add spelling, grammar, or stylistic checks.

- The reference pages are generated output. Prefer changing the source Markdown or generator code rather than editing `docs/sctrl.md`, `docs/triggers.md`, or `docs/redirections.md` directly. `docs/index.md` is generated from `static/index_template.md` by the workflow when reference content changes.
- `merge_lib.py::rewrite_links` maps known trigger/state-controller wiki pages to the generated Pages routes, preserves source heading anchors (including mapped legacy aliases), and sends other extensionless relative wiki-page links to the upstream wiki. Relative paths with file extensions are left alone as likely assets.
- Generators fail on missing required sections or empty parsed reference entries instead of writing obviously incomplete output. Review these guards when upstream headings change.
- `tests/` contains standard-library tests for merger behavior. CI runs these tests and `validate_docs.py`, which checks generated-page structure and internal routes/anchors; it is not a language or style linter.
- `.github/workflows/update.yml` pins actions by commit SHA and installs exact Python dependency versions from `requirements.txt`. Keep these versions reviewed and updated deliberately.

## Validation

At the follow-up on 2026-09-23, 15 standard-library unit tests passed, all three generators completed against the live wiki, and `python validate_docs.py` passed. `python -m compileall` also passed. `git diff --check` reports trailing spaces in regenerated Markdown inherited from the source docs; these spaces encode Markdown line breaks, so don’t strip them indiscriminately.

## Audit baseline (time-sensitive)

At that audit, local `main` was 12 commits behind its available `origin/main` reference. The intervening commits changed generated documentation pages; no generator or workflow files appeared in the diff. The local landing-page timestamp was 2026-07-31, while `origin/main` showed 2026-09-20. Recheck Git state and remote content before relying on these branch and timestamp details.
