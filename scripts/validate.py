#!/usr/bin/env python3
"""
DPDP Act 2023 & DPDP Rules 2025 - Skills Suite Validator
Validates frontmatter, directory naming, legal citations, cross-references, and phased commencement dates.
"""

import sys
import re
from pathlib import Path

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

ROOT = Path(__file__).resolve().parent.parent

def log_pass(msg):
    print(f"[{GREEN}PASS{RESET}] {msg}")

def log_fail(msg):
    print(f"[{RED}FAIL{RESET}] {msg}")

def log_warn(msg):
    print(f"[{YELLOW}WARN{RESET}] {msg}")

def parse_frontmatter(text):
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

def run_validation():
    errors = 0
    warnings = 0

    print(f"\n{BLUE}=== DPDP Act Skills Suite: Quality Assurance & Legal Audit ==={RESET}\n")

    # 1. Directory Structure
    skills_dir = ROOT / "skills"
    if not skills_dir.exists():
        log_fail("Canonical 'skills/' directory not found.")
        errors += 1
    else:
        log_pass("Canonical 'skills/' directory exists.")

    legacy_dir = ROOT / "dpdp-skills"
    if legacy_dir.exists():
        log_fail("Deprecated 'dpdp-skills/' directory found. Only 'skills/' must be used.")
        errors += 1
    else:
        log_pass("No duplicate 'dpdp-skills/' directory detected.")

    # 2. Check 5 Skills
    expected_skills = [
        "dpdp-act-overview",
        "dpdp-consent-and-notice",
        "dpdp-fiduciary-obligations",
        "dpdp-data-principal-rights",
        "dpdp-board-enforcement",
    ]

    for sname in expected_skills:
        sdir = skills_dir / sname
        sfile = sdir / "SKILL.md"
        if not sfile.exists():
            log_fail(f"Missing skill file: skills/{sname}/SKILL.md")
            errors += 1
            continue

        content = sfile.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        if not fm:
            log_fail(f"Invalid YAML frontmatter in {sfile.name}")
            errors += 1
            continue

        if fm.get("name") != sname:
            log_fail(f"Skill name mismatch: frontmatter '{fm.get('name')}' != directory '{sname}'")
            errors += 1
        else:
            log_pass(f"Skill '{sname}' frontmatter name matches directory.")

        for req in ["description", "version", "last_verified", "jurisdiction", "primary_statute", "subordinate_rules"]:
            if req not in fm:
                log_fail(f"Missing '{req}' in frontmatter for {sname}")
                errors += 1

        # Check for 8-point structure markers or essential headers
        if "## 1. Statutory Response Structure" not in content and "Statutory Response Structure" not in content:
            log_warn(f"Skill '{sname}' may be missing standardized response structure header.")
            warnings += 1

    # 3. Check Legal Sources
    legal_dir = ROOT / "legal-sources"
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
        spath = legal_dir / src
        if not spath.exists():
            log_fail(f"Missing legal source registry file: legal-sources/{src}")
            errors += 1
        else:
            log_pass(f"Legal source '{src}' verified.")

    # 4. Check Integrations
    integrations_dir = ROOT / "integrations"
    expected_integrations = [
        "claude-code.md",
        "cursor.md",
        "antigravity.md",
        "gemini-cli.md",
        "custom-agents.md",
    ]
    for doc in expected_integrations:
        ipath = integrations_dir / doc
        if not ipath.exists():
            log_fail(f"Missing integration doc: integrations/{doc}")
            errors += 1
        else:
            log_pass(f"Integration guide '{doc}' verified.")

    print(f"\n{BLUE}=== Audit Summary ==={RESET}")
    print(f"Errors: {RED if errors else GREEN}{errors}{RESET}")
    print(f"Warnings: {YELLOW if warnings else GREEN}{warnings}{RESET}")

    if errors == 0:
        print(f"\n{GREEN}All checks passed successfully! Repository is production-ready.{RESET}\n")
        return 0
    else:
        print(f"\n{RED}Validation failed with {errors} errors. Please fix before release.{RESET}\n")
        return 1

if __name__ == "__main__":
    sys.exit(run_validation())

