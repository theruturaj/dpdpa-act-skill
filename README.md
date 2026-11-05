# DPDP Act Skills Suite: India Digital Personal Data Protection Act, 2023 & Rules 2025

[![Skills Validation](https://github.com/theruturaj/dpdp-act-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/theruturaj/dpdp-act-skills/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Legal Jurisdiction](https://img.shields.io/badge/Jurisdiction-India%20(IN)-blue.svg)](legal-sources/act-2023-source.md)
[![Enforcement Status](https://img.shields.io/badge/Status-Phased%20Commencement-orange.svg)](legal-sources/commencement-notification.md)

Production-grade, verified **AI Agent Skills** for India's **Digital Personal Data Protection Act, 2023** (Act No. 22 of 2023) and the **Digital Personal Data Protection Rules, 2025** (notified November 2025; corrigendum December 2025).

Designed for zero-dependency integration into **Claude Code**, **Google Antigravity**, **Cursor IDE**, **Gemini CLI**, and custom LLM agent pipelines.

---

## 🏛️ Statutory Baseline & Phased Enforcement

This repository is **reconciled against official Gazette publications** from the Ministry of Electronics and Information Technology (MeitY), Government of India:

- **Primary Statute**: *The Digital Personal Data Protection Act, 2023* (Act No. 22 of 2023; Assent 11 August 2023).
- **Subordinate Legislation**: *The Digital Personal Data Protection Rules, 2025* (Notified 13 November 2025; Corrigendum 16 December 2025).
- **Phased Commencement**: *Notification G.S.R. 843(E)* establishes three enforcement phases:
  - **Phase 1 (13 November 2025 — IN FORCE)**: Section 1, Section 2 (all definitions), Sections 18–26 (Data Protection Board of India establishment), Section 30 (Consolidated Fund), Section 34 (MeitY info powers), Sections 40–41 (Rule-making), Section 43 (Removal of difficulties), and Rules 1, 2, 17–21.
  - **Phase 2 (13 November 2026 — COMMENCING SOON)**: Section 6(9) (Consent Manager registration & obligations), Section 27(1)(d) (Board inquiry into Consent Managers), and Rule 4 (Consent Manager technical & operational standards).
  - **Phase 3 (13 May 2027 — FUTURE COMMENCEMENT)**: Sections 3–17 (Notice, consent, legitimate uses, fiduciary duties, children's data, SDFs, Data Principal rights, cross-border transfers, exemptions), Sections 27(1)(a)-(c), 28–29, 31–33, 35–39, 42, 44, the Schedule (Penalties), and Rules 3, 5–16, 22–23.
- **Board Establishment**: *Notification G.S.R. 844(E)* establishing the Data Protection Board of India.

---

## 📦 The Five Categorized Skills

The Act and Rules are divided into five modular, independent skills:

| Skill | Canonical Path | Primary Sections & Rules | Key Coverage |
|---|---|---|---|
| **`dpdp-act-overview`** | [`skills/dpdp-act-overview/SKILL.md`](skills/dpdp-act-overview/SKILL.md) | Sections 1–3, Rules 1–2 | Material and territorial scope (s.3), extraterritorial applicability, 26 key definitions (s.2), phased commencement tracking, and master routing table pointing to the other four skills. |
| **`dpdp-consent-and-notice`** | [`skills/dpdp-consent-and-notice/SKILL.md`](skills/dpdp-consent-and-notice/SKILL.md) | Sections 4–7, Rules 3–4 | Lawful processing grounds, mandatory 3-part notice requirements, 22 Eighth Schedule language options, valid consent standards (free, specific, informed, unconditional), unbundling rules, withdrawal parity, Consent Manager architecture, and statutory legitimate uses (s.7). |
| **`dpdp-fiduciary-obligations`** | [`skills/dpdp-fiduciary-obligations/SKILL.md`](skills/dpdp-fiduciary-obligations/SKILL.md) | Sections 8–10, Rules 5–9 | General fiduciary obligations, vendor Data Processing Agreements (DPAs), reasonable security safeguards (s.8(5)), dual breach intimation to Board and Principals (s.8(6)), purpose-linked retention and erasure timelines (s.8(7)), verifiable parental consent for children under 18 (s.9), ban on child tracking/targeted ads, and Significant Data Fiduciary (SDF) requirements (DPO, Independent Auditor, DPIA). |
| **`dpdp-data-principal-rights`** | [`skills/dpdp-data-principal-rights/SKILL.md`](skills/dpdp-data-principal-rights/SKILL.md) | Sections 11–15, Rules 10–12 | Individual rights: access to summaries and sharing identities (s.11), correction/completion/updating/erasure (s.12), mandatory grievance redressal exhaustion (s.13), nomination procedures (s.14), and statutory duties of Data Principals carrying penalties up to ₹10,000 (s.15). |
| **`dpdp-board-enforcement`** | [`skills/dpdp-board-enforcement/SKILL.md`](skills/dpdp-board-enforcement/SKILL.md) | Sections 16–44, Schedule, Rules 13–16, 22–23 | Cross-border transfer negative list regime (s.16), statutory exemptions (s.17: judicial, law enforcement, research, BPO/foreign contracts, startups), Data Protection Board powers and digital inquiry procedure (ss.18–28), mediation (s.31), voluntary undertakings (s.32), TDSAT appeals (s.29), complete penalty Schedule (up to ₹250 crore), and consequential amendments (TRAI Act, IT Act s.43A omission, RTI Act s.8(1)(j) substitution). |

---

## 🔍 Verification & Quality Assurance Checks

Every skill in this repository has been audited against strict quality standards:

1. **Frontmatter & Folder Conformance**:
   - Every skill lives under `skills/<skill-name>/SKILL.md`.
   - Each skill contains standard YAML frontmatter (`name`, `description`, `version`, `last_verified`, `jurisdiction`, `primary_statute`, `subordinate_rules`, `commencement_status`).
2. **Statutory & Gazette Alignment**:
   - All citations match the official Gazette texts (Act No. 22 of 2023, DPDP Rules 2025, G.S.R. 843(E), G.S.R. 844(E), Corrigendum).
   - Penalties match the statutory Schedule (₹250 cr for safeguards failure, ₹200 cr for breach notification failure, ₹200 cr for children's violations, ₹150 cr for SDF breaches, ₹10,000 for Principal duty violations).
   - Limitation periods verified (60 days for TDSAT appeals under s.29; 6-month disposal benchmark).
   - Section 17 exemptions categorized accurately across judicial, state security, research, startup, and foreign outsourcing categories.
3. **No Hallucinated Delegated Rules**:
   - Rules are strictly verified against the Gazette of India. Where operational thresholds remain to be notified, they are explicitly designated as "as may be prescribed".
4. **Phased Commencement Guardrails**:
   - AI agents are prevented from presenting future Phase 3 requirements (commencing 13 May 2027) as already enforceable obligations today.

---

## ⚖️ Standardized 8-Point Legal Response Framework

Each skill instructs the AI agent to format legal responses using an 8-point structure:

1. **Legal Provision**: Section of the DPDP Act, 2023 and clause of the DPDP Rules, 2025.
2. **Plain-Language Interpretation**: Clear explanation of statutory expectations.
3. **Applicable DPDP Rule**: Procedural standards, forms, or notification windows.
4. **Commencement Status**: State whether provision is in Phase 1 (In Force), Phase 2 (Nov 2026), or Phase 3 (May 2027).
5. **Compliance Implications**: Technical, operational, and organizational actions required.
6. **Exceptions & Exemptions**: Carve-outs under Section 17 or statutory provisos.
7. **Official Source References**: Citations to Gazette notification numbers and legal sources.
8. **Legal Uncertainty & Interpretive Limitations**: Flags for pending notifications or judicial precedent.

---

## 🚀 Quick Start & Integrations

Comprehensive integration guides are available in the [`integrations/`](integrations/) directory:

- [Claude Code Integration Guide](integrations/claude-code.md)
- [Cursor IDE Integration Guide](integrations/cursor.md)
- [Google Antigravity Integration Guide](integrations/antigravity.md)
- [Gemini CLI Integration Guide](integrations/gemini-cli.md)
- [Custom Agents & Python SDK Guide](integrations/custom-agents.md)

### One-line Install for Claude Code:
```bash
git clone https://github.com/theruturaj/dpdp-act-skills.git
mkdir -p ~/.claude/skills
cp -r dpdp-act-skills/skills/* ~/.claude/skills/
```

### One-line Install for Antigravity:
```bash
git clone https://github.com/theruturaj/dpdp-act-skills.git
mkdir -p ~/.gemini/config/skills
cp -r dpdp-act-skills/skills/* ~/.gemini/config/skills/
```

---

## 🧪 Testing & Validation

The repository includes a comprehensive test suite in `tests/` and a standalone audit script:

```bash
# Run standalone QA validator
python3 scripts/validate.py

# Run unit tests
python3 -m unittest discover tests
```

---

## 📁 Repository Structure

```
dpdp-act-skills/
├── .github/
│   ├── workflows/
│   │   └── validate-skills.yml     # Automated CI verification
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── legal_update.md         # Template for reporting statutory updates
│   │   └── skill_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── skills/                         # Canonical AI Agent Skills
│   ├── dpdp-act-overview/SKILL.md
│   ├── dpdp-consent-and-notice/SKILL.md
│   ├── dpdp-fiduciary-obligations/SKILL.md
│   ├── dpdp-data-principal-rights/SKILL.md
│   └── dpdp-board-enforcement/SKILL.md
├── legal-sources/                  # Primary Gazette & statutory registry
│   ├── README.md
│   ├── act-2023-source.md
│   ├── rules-2025-source.md
│   ├── commencement-notification.md
│   ├── board-establishment-notification.md
│   ├── corrigendum-dec-2025.md
│   └── legal-status.yml            # Machine-readable source of truth
├── integrations/                   # Platform-specific integration docs
│   ├── claude-code.md
│   ├── cursor.md
│   ├── antigravity.md
│   ├── gemini-cli.md
│   └── custom-agents.md
├── tests/                          # Automated unit tests
│   ├── test_directory_structure.py
│   ├── test_frontmatter.py
│   ├── test_skill_references.py
│   └── test_legal_sources.py
├── scripts/
│   └── validate.py                 # Standalone validation CLI
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE                         # MIT License
├── README.md
├── SECURITY.md
└── pyproject.toml
```

---

## 📜 Disclaimer

*This repository provides structured reference material for software engineers, compliance architects, and AI agents. It does not constitute formal legal advice. For organizational compliance or litigation representation, consult a qualified advocate or privacy counsel registered in India.*

---

## 📄 License

Distributed under the [MIT License](LICENSE). Copyright (c) 2026 Ruturaj Jarag.

