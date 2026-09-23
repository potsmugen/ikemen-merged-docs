import tempfile
import unittest
from pathlib import Path

from merge_lib import (
    clean_heading,
    hide_code_blocks,
    require_entries,
    require_sections,
    rewrite_links,
    tag_first_heading,
)
from validate_docs import validate_generated_docs


class RewriteLinksTests(unittest.TestCase):
    def test_rewrites_trailing_slash_and_tagged_trigger_anchor(self):
        self.assertEqual(
            rewrite_links("[TeamLeader](Triggers/#new_teamleader)"),
            "[TeamLeader](triggers#new_teamleader)",
        )

    def test_rewrites_parent_relative_state_controller_link(self):
        self.assertEqual(
            rewrite_links(
                "[ChangeState](../State-controllers-(changed)/#changed_changestate)"
            ),
            "[ChangeState](sctrl#changed_changestate)",
        )

    def test_tagging_preserves_source_anchor_ids(self):
        self.assertEqual(
            tag_first_heading('## <a name="new_tagout">TagOut</a>', "(new)"),
            '## <a name="new_tagout">TagOut (new)</a>',
        )

    def test_clean_heading_preserves_nightly_build_qualifier(self):
        self.assertEqual(
            clean_heading("Feature (nightly build only)"),
            "Feature (nightly build only)",
        )

    def test_tagging_preserves_nightly_build_qualifier(self):
        self.assertEqual(
            tag_first_heading("## Feature (nightly build only)", "(new)"),
            "## Feature (nightly build only) (new)",
        )

    def test_maps_upstream_anchor_aliases_and_preserves_stale_wiki_targets(self):
        self.assertEqual(
            rewrite_links(
                "[GetHitVarSet](State-controllers-(new)/#new_gethitvarset)"
            ),
            "[GetHitVarSet](sctrl#new_grthitvarset)",
        )
        self.assertEqual(
            rewrite_links(
                "[PlatformAngle](State-controllers-(changed)/#changed_projectile_platformangle)"
            ),
            "[PlatformAngle](https://github.com/ikemen-engine/Ikemen-GO/wiki/State-controllers-(changed)#changed_projectile_platformangle)",
        )

    def test_trigger_redirection_links_target_the_redirections_page(self):
        self.assertEqual(
            rewrite_links("[PlayerIndex](Triggers-(new)/#redirection_playerindex)"),
            "[PlayerIndex](redirections#playerindexn-new)",
        )

    def test_other_wiki_pages_become_absolute_wiki_links(self):
        self.assertEqual(
            rewrite_links("[Action](Lifebar-features/#new_action)"),
            "[Action](https://github.com/ikemen-engine/Ikemen-GO/wiki/Lifebar-features#new_action)",
        )

    def test_absolute_links_anchors_and_file_paths_are_unchanged(self):
        source = (
            "[web](https://example.com/a) [anchor](#local) "
            "![image](../assets/example.png)"
        )
        self.assertEqual(rewrite_links(source), source)


class SourceValidationTests(unittest.TestCase):
    def test_required_section_must_exist(self):
        with self.assertRaisesRegex(ValueError, "missing required section"):
            require_sections({"Existing": "content"}, ["Expected"], "source")

    def test_required_section_must_have_content(self):
        with self.assertRaisesRegex(ValueError, "empty required section"):
            require_sections({"Expected": "## Expected"}, ["Expected"], "source")

    def test_source_with_only_a_heading_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "no documented sections"):
            require_sections({"Title": "# Title"}, [], "source")

    def test_entry_validation_rejects_heading_only_blocks(self):
        with self.assertRaisesRegex(ValueError, "no documented entries"):
            require_entries({"Heading": "## Heading"}, "source")

    def test_fenced_code_headings_are_not_parsed_as_document_sections(self):
        text, placeholders = hide_code_blocks("```md\n## Example\n```\n## Real")
        self.assertIn("## Real", text)
        self.assertNotIn("## Example", text)
        self.assertEqual(len(placeholders), 1)


class GeneratedDocsValidationTests(unittest.TestCase):
    def test_validates_expected_pages_and_internal_routes(self):
        with tempfile.TemporaryDirectory() as directory:
            docs = Path(directory)
            for filename, title in {
                "sctrl.md": "State Controller Reference",
                "triggers.md": "Trigger Reference",
                "redirections.md": "Trigger Redirection Reference",
            }.items():
                content = f"# {title}\n\n## Table of Contents\n\n## Example\n"
                if filename == "triggers.md":
                    content += "\n<a id=\"new_teamleader\"></a>\n## TeamLeader (new)\n"
                (docs / filename).write_text(content, encoding="utf-8")
            (docs / "sctrl.md").write_text(
                (docs / "sctrl.md").read_text(encoding="utf-8")
                + "\n[Triggers](triggers#new_teamleader)\n",
                encoding="utf-8",
            )
            validate_generated_docs(docs)

    def test_rejects_missing_internal_anchors(self):
        with tempfile.TemporaryDirectory() as directory:
            docs = Path(directory)
            for filename, title in {
                "sctrl.md": "State Controller Reference",
                "triggers.md": "Trigger Reference",
                "redirections.md": "Trigger Redirection Reference",
            }.items():
                (docs / filename).write_text(
                    f"# {title}\n\n## Table of Contents\n\n## Example\n",
                    encoding="utf-8",
                )
            (docs / "sctrl.md").write_text(
                (docs / "sctrl.md").read_text(encoding="utf-8")
                + "\n[Triggers](triggers#missing-anchor)\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "anchor .* is missing"):
                validate_generated_docs(docs)

    def test_rejects_unresolved_relative_wiki_page_links(self):
        with tempfile.TemporaryDirectory() as directory:
            docs = Path(directory)
            for filename, title in {
                "sctrl.md": "State Controller Reference",
                "triggers.md": "Trigger Reference",
                "redirections.md": "Trigger Redirection Reference",
            }.items():
                (docs / filename).write_text(
                    f"# {title}\n\n## Table of Contents\n\n## Example\n",
                    encoding="utf-8",
                )
            (docs / "sctrl.md").write_text(
                (docs / "sctrl.md").read_text(encoding="utf-8")
                + "\n[Feature](Unknown-wiki-page/#new_feature)\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "unresolved relative page link"):
                validate_generated_docs(docs)


if __name__ == "__main__":
    unittest.main()
