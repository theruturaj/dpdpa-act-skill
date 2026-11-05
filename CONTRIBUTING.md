# Contributing to the DPDP Act Skills Suite

Thank you for your interest in contributing to the **DPDP Act Skills Suite**! This repository aims to maintain the highest standard of legal accuracy and AI agent usability for India's data protection regime.

---

## 🏛️ Guiding Principles for Contributions

1. **Statutory Verifiability**: Every factual assertion must be directly grounded in the official Gazette of India publication of the *Digital Personal Data Protection Act, 2023*, the *DPDP Rules, 2025*, or official Central Government notifications.
2. **No Speculation on Un-notified Standards**: Where subordinate rules or administrative thresholds have not yet been notified, state that they are "as may be prescribed". Never invent or guess procedural specifics.
3. **Phased Commencement Awareness**: Always account for the enforcement phases established under Notification G.S.R. 843(E) (Phase 1: 13 Nov 2025, Phase 2: 13 Nov 2026, Phase 3: 13 May 2027).
4. **Platform Independence**: Skill knowledge in `skills/` must remain portable and free of platform-specific runtime assumptions. Platform guides belong in `integrations/`.

---

## 🛠️ How to Report Statutory Updates or Rule Changes

As MeitY, the Central Government, or the Data Protection Board of India issue new notifications:
1. Open an issue using the [Legal Update Template](.github/ISSUE_TEMPLATE/legal_update.md).
2. Cite the exact Gazette reference, notification number (e.g. `G.S.R. XXX(E)`), publication date, and official MeitY URL.
3. Specify which sections or rules are impacted and whether `legal-sources/legal-status.yml` needs an update.

---

## 🧪 Development & Quality Workflow

Before submitting a Pull Request:

1. **Run the QA Validator**:
   ```bash
   python3 scripts/validate.py
   ```
2. **Run Unit Tests**:
   ```bash
   python3 -m unittest discover tests
   ```
3. **Verify Frontmatter**:
   - Ensure `name` matches the directory name under `skills/`.
   - Update `last_verified` to the date of your verification.
   - Maintain valid YAML structure.
4. **Follow the PR Template**: Use [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md) when opening your PR.

---

## 📄 Licensing

By contributing to this repository, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
