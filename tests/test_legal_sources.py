import unittest
from pathlib import Path

class TestLegalSources(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent
        self.legal_dir = self.root / "legal-sources"

    def test_legal_status_yml_content(self):
        status_file = self.legal_dir / "legal-status.yml"
        self.assertTrue(status_file.exists())
        content = status_file.read_text(encoding="utf-8")

        # Must mention the 3 phases and their effective dates
        self.assertIn("phase_1:", content)
        self.assertIn("2025-11-13", content)
        self.assertIn("phase_2:", content)
        self.assertIn("2026-11-13", content)
        self.assertIn("phase_3:", content)
        self.assertIn("2027-05-13", content)
        self.assertIn("G.S.R. 843(E)", content)
        self.assertIn("G.S.R. 844(E)", content)

    def test_sources_contain_official_urls(self):
        act_source = (self.legal_dir / "act-2023-source.md").read_text(encoding="utf-8")
        self.assertIn("https://www.meity.gov.in", act_source)

        rules_source = (self.legal_dir / "rules-2025-source.md").read_text(encoding="utf-8")
        self.assertIn("https://www.meity.gov.in", rules_source)

        commencement_source = (self.legal_dir / "commencement-notification.md").read_text(encoding="utf-8")
        self.assertIn("G.S.R. 843(E)", commencement_source)

        board_source = (self.legal_dir / "board-establishment-notification.md").read_text(encoding="utf-8")
        self.assertIn("G.S.R. 844(E)", board_source)

        corrigendum_source = (self.legal_dir / "corrigendum-dec-2025.md").read_text(encoding="utf-8")
        self.assertIn("16 December 2025", corrigendum_source)

if __name__ == "__main__":
    unittest.main()

