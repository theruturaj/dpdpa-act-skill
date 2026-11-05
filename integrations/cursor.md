# Cursor IDE Integration Guide

This guide explains how to integrate the **DPDP Act 2023 & Rules 2025** skills into the **Cursor IDE** using `.cursorrules` or `.cursor/rules`.

---

## 1. Directory Setup

You can place the skills directly in your repository under `.cursor/skills/` or `skills/`:

```bash
git clone https://github.com/theruturaj/dpdp-act-skills.git
mkdir -p your-project/.cursor/skills
cp -r dpdp-act-skills/skills/* your-project/.cursor/skills/
```

---

## 2. Cursor Rules Configuration

Create a file named `.cursor/rules/dpdp-compliance.mdc` (or add to `.cursorrules` in your project root):

```markdown
---
description: Enforce legal accuracy and phased compliance under India's DPDP Act, 2023 and DPDP Rules, 2025
globs: ["**/*.ts", "**/*.tsx", "**/*.py", "**/*.go", "**/privacy*", "**/consent*", "**/terms*"]
---

# DPDP Act, 2023 Compliance Assistant

You have access to the verified statutory skills in `.cursor/skills/`:
- `dpdp-act-overview`: Master router, scope (s.3), definitions (s.2), phased commencement.
- `dpdp-consent-and-notice`: Notice standards (s.5, Rule 3), consent (s.6), Consent Managers (Rule 4), legitimate uses (s.7).
- `dpdp-fiduciary-obligations`: Security (s.8(5), Rule 6), breach notification (s.8(6), Rule 7), children (s.9, Rule 5), SDFs (s.10, Rule 9).
- `dpdp-data-principal-rights`: Rights to access, correction, erasure (ss.11-14, Rules 10-12), and Principal duties (s.15).
- `dpdp-board-enforcement`: Cross-border transfers (s.16, Rule 13), exemptions (s.17), Board inquiries (ss.27-28), TDSAT appeals (s.29), and penalties Schedule.

## Mandatory Rules:
1. Ground every compliance recommendation in exact Section numbers and DPDP Rules, 2025 clauses.
2. Delineate phased commencement:
   - Phase 1 (13 Nov 2025): Definitions & Board creation (IN FORCE).
   - Phase 2 (13 Nov 2026): Consent Manager framework (COMMENCING SOON).
   - Phase 3 (13 May 2027): Substantive fiduciary obligations, citizen rights, and penalties.
3. Structure responses with: Provision, Plain interpretation, Applicable Rule, Commencement status, Compliance implications, Exceptions, and Limitations.
```
