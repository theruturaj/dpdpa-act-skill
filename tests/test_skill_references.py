import re
import unittest
from pathlib import Path

class TestSkillReferences(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent
        self.skills_dir = self.root / "skills"
        self.skill_names = {
            "dpdp-act-overview",
            "dpdp-consent-and-notice",
            "dpdp-fiduciary-obligations",
            "dpdp-data-principal-rights",
            "dpdp-board-enforcement",
        }

    def test_overview_routes_to_all_other_skills(self):
        overview_file = self.skills_dir / "dpdp-act-overview" / "SKILL.md"
        content = overview_file.read_text(encoding="utf-8")
        
        # Router table must reference the other 4 skills
        for target_skill in self.skill_names - {"dpdp-act-overview"}:
            self.assertIn(f"`{target_skill}`", content, f"Router in dpdp-act-overview must mention `{target_skill}`")

    def test_each_skill_contains_cross_references(self):
        for sname in self.skill_names:
            skill_file = self.skills_dir / sname / "SKILL.md"
            content = skill_file.read_text(encoding="utf-8")
            
            # Each skill should reference at least two other skills
            refs_found = [other for other in self.skill_names if other != sname and f"`{other}`" in content]
            self.assertTrue(len(refs_found) >= 2, f"Skill {sname} should cross-reference at least two other skills, found: {refs_found}")

    def test_statutory_sections_mentioned(self):
        # Validate that essential statutory sections are covered across the suite
        sections_to_check = {
            "dpdp-act-overview": ["Section 3", "Section 2"],
            "dpdp-consent-and-notice": ["Section 4", "Section 5", "Section 6", "Section 7"],
            "dpdp-fiduciary-obligations": ["Section 8", "Section 9", "Section 10"],
            "dpdp-data-principal-rights": ["Section 11", "Section 12", "Section 13", "Section 14", "Section 15"],
            "dpdp-board-enforcement": ["Section 16", "Section 17", "Section 18", "Section 27", "Section 29", "Section 33"],
        }
        for sname, expected_sections in sections_to_check.items():
            skill_file = self.skills_dir / sname / "SKILL.md"
            content = skill_file.read_text(encoding="utf-8")
            for sec in expected_sections:
                self.assertTrue(
                    sec in content or sec.lower() in content.lower(),
                    f"Skill {sname} should cite {sec}"
                )

if __name__ == "__main__":
    unittest.main()
