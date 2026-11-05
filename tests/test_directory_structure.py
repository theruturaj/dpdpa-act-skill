import os
import unittest
from pathlib import Path

class TestDirectoryStructure(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent

    def test_canonical_skills_exist(self):
        skills_dir = self.root / "skills"
        self.assertTrue(skills_dir.exists() and skills_dir.is_dir(), "skills/ directory must exist")
        
        expected_skills = [
            "dpdp-act-overview",
            "dpdp-consent-and-notice",
            "dpdp-fiduciary-obligations",
            "dpdp-data-principal-rights",
            "dpdp-board-enforcement",
        ]
        for skill in expected_skills:
            skill_md = skills_dir / skill / "SKILL.md"
            self.assertTrue(skill_md.exists(), f"Skill file {skill_md} must exist")

    def test_no_duplicate_dpdp_skills_dir(self):
        legacy_dir = self.root / "dpdp-skills"
        self.assertFalse(legacy_dir.exists(), "dpdp-skills/ directory must not exist (must use canonical skills/)")

    def test_legal_sources_exist(self):
        legal_sources_dir = self.root / "legal-sources"
        self.assertTrue(legal_sources_dir.exists() and legal_sources_dir.is_dir())
        
        expected_sources = [
            "README.md",
            "act-2023-source.md",
            "rules-2025-source.md",
            "commencement-notification.md",
            "board-establishment-notification.md",
            "corrigendum-dec-2025.md",
            "legal-status.yml",
        ]
        for src in expected_sources:
            src_path = legal_sources_dir / src
            self.assertTrue(src_path.exists(), f"Legal source file {src} must exist")

    def test_integrations_exist(self):
        integrations_dir = self.root / "integrations"
        self.assertTrue(integrations_dir.exists() and integrations_dir.is_dir())
        
        expected_integrations = [
            "claude-code.md",
            "cursor.md",
            "antigravity.md",
            "gemini-cli.md",
            "custom-agents.md",
        ]
        for doc in expected_integrations:
            doc_path = integrations_dir / doc
            self.assertTrue(doc_path.exists(), f"Integration guide {doc} must exist")

    def test_root_files_exist(self):
        for fname in ["README.md", "LICENSE", ".gitignore", "CONTRIBUTING.md", "CHANGELOG.md", "SECURITY.md"]:
            path = self.root / fname
            self.assertTrue(path.exists(), f"Root file {fname} must exist")

if __name__ == "__main__":
    unittest.main()
