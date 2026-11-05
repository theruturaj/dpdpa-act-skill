# Google Antigravity Integration Guide

This guide explains how to install and leverage the **DPDP Act 2023 & Rules 2025** skills in **Google Antigravity**.

---

## 1. Skill Installation

Install the skills to your Antigravity user configuration directory:

```bash
# Clone the repository
git clone https://github.com/theruturaj/dpdp-act-skills.git

# Copy into Antigravity skills directory
mkdir -p ~/.gemini/config/skills
cp -r dpdp-act-skills/skills/* ~/.gemini/config/skills/
```

Antigravity automatically indexes any skill directory containing a `SKILL.md` with YAML frontmatter.

---

## 2. Using the Skills in Conversations

Antigravity auto-activates the skills based on conversation context:
- Whenever you mention terms like "DPDPA", "DPDP Act", "personal data breach India", "Consent Manager", or "Section 8(5)", Antigravity consults the skills.
- The router skill `dpdp-act-overview` automatically identifies which specialized skill covers the issue.

---

## 3. Custom Rule Configuration

To enforce DPDP compliance verification rules globally in Antigravity, add this rule file to `~/.gemini/config/rules/dpdp.md`:

```markdown
# Rule: India DPDP Act 2023 & DPDP Rules 2025 Standard

When generating code, architecture, or policy documents that touch digital personal data of Indian residents:
1. Ensure architecture supports independent notice and unbundled consent per Sections 5 and 6 of the DPDP Act.
2. Ensure personal data breach notification can be dispatched within the timelines prescribed by Rule 7.
3. Validate user age verification safeguards if handling data of children under 18 (Section 9 & Rule 5).
4. Strictly track enforcement phases under G.S.R. 843(E) (Phase 1: 13 Nov 2025; Phase 2: 13 Nov 2026; Phase 3: 13 May 2027).
```
