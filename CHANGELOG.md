# Changelog

All notable changes to the **DPDP Act Skills Suite** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-11-05

### Added
- **Canonical Skill Architecture**: Initial release of 5 modular, production-ready AI agent skills under `skills/`:
  - `dpdp-act-overview`: Master router, scope (s.3), definitions (s.2), and phased commencement.
  - `dpdp-consent-and-notice`: Notice standards (s.5, Rule 3), consent mechanics (s.6), Consent Managers (Rule 4), and legitimate uses (s.7).
  - `dpdp-fiduciary-obligations`: Security safeguards (s.8(5), Rule 6), breach intimation (s.8(6), Rule 7), retention/erasure (s.8(7), Rule 8), child data protection (s.9, Rule 5), and Significant Data Fiduciaries (s.10, Rule 9).
  - `dpdp-data-principal-rights`: Information access (s.11), correction/erasure (s.12), grievance redressal (s.13), nomination (s.14), and statutory individual duties carrying penalties up to ₹10,000 (s.15).
  - `dpdp-board-enforcement`: Cross-border transfers (s.16, Rule 13), statutory exemptions (s.17, Rule 14), Board digital inquiry procedure (ss.18–28, Rule 15), mediation (s.31), voluntary undertakings (s.32), TDSAT appeals (s.29, Rule 22), complete penalty Schedule (up to ₹250 crore), and consequential amendments.
- **Legal Reconciliation**:
  - Reconciled with the *Digital Personal Data Protection Act, 2023* (Act No. 22 of 2023).
  - Reconciled with the *Digital Personal Data Protection Rules, 2025* (Notified 13 November 2025).
  - Incorporated the *Phased Commencement Notification G.S.R. 843(E)* establishing three enforcement tiers (Phase 1: 13 Nov 2025, Phase 2: 13 Nov 2026, Phase 3: 13 May 2027).
  - Incorporated the *Board Establishment Notification G.S.R. 844(E)* establishing the Data Protection Board of India.
  - Incorporated the *MeitY Corrigendum to the DPDP Rules, 2025* (16 December 2025).
- **Statutory Legal Registry**: Added `legal-sources/` with full metadata and official Gazette links.
- **Machine-Readable Truth**: Added `legal-sources/legal-status.yml` tracking section-by-section and rule-by-rule enforcement phases.
- **Standardized Legal Response Structure**: Embedded the mandatory 8-point statutory response format across all skills.
- **Agent Interoperability Guides**: Added integration walkthroughs for Claude Code, Cursor IDE, Google Antigravity, Gemini CLI, and Custom Agent frameworks under `integrations/`.
- **Automated Validation**:
  - Python unit test suite in `tests/` (`test_frontmatter.py`, `test_directory_structure.py`, `test_skill_references.py`, `test_legal_sources.py`).
  - Standalone CLI validator script `scripts/validate.py`.
  - GitHub Actions CI workflow `.github/workflows/validate-skills.yml`.
- **Open-Source Standards**: Added MIT License, `CONTRIBUTING.md`, `SECURITY.md`, and GitHub issue/PR templates.

