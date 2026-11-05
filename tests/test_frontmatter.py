import os
import re
import unittest
from pathlib import Path

class TestFrontmatter(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent
        self.skills_dir = self.root / "skills"

    def parse_frontmatter(self, text):
        match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not match:
            return None
        raw = match.group(1)
        data = {}
        for line in raw.strip().split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                k, v = line.split(":", 1)
                data[k.strip()] = v.strip().strip('"').strip("'")
        return data

    def test_all_skills_have_valid_frontmatter(self):
        skill_dirs = [d for d in self.skills_dir.iterdir() if d.is_dir()]
        self.assertEqual(len(skill_dirs), 5, "Must have exactly 5 skills")

        required_fields = [
            "name",
            "description",
            "version",
            "last_verified",
            "jurisdiction",
            "primary_statute",
            "subordinate_rules",
            "commencement_status",
        ]

        for sdir in skill_dirs:
            skill_file = sdir / "SKILL.md"
            self.assertTrue(skill_file.exists(), f"SKILL.md missing in {sdir}")
            content = skill_file.read_text(encoding="utf-8")
            fm = self.parse_frontmatter(content)
            self.assertIsNotNone(fm, f"Frontmatter invalid or missing in {skill_file}")

            # Check name matches directory name
            self.assertEqual(fm.get("name"), sdir.name, f"Skill name '{fm.get('name')}' must match folder '{sdir.name}'")

            # Check all required fields are present and non-empty
            for field in required_fields:
                self.assertIn(field, fm, f"Field '{field}' missing in frontmatter of {skill_file}")
                self.assertTrue(len(fm[field]) > 0, f"Field '{field}' in {skill_file} cannot be empty")

            # Check jurisdiction is IN
            self.assertEqual(fm.get("jurisdiction"), "IN")

if __name__ == "__main__":
    unittest.main()

