# Claude Code Integration Guide

This guide explains how to install and invoke the **India DPDP Act 2023 & Rules 2025** skills suite in **Claude Code**.

---

## 1. Installation

### Option A: Install into User Global Skills Directory
To make the DPDP skills available across all your Claude Code sessions:

```bash
# Clone the repository
git clone https://github.com/theruturaj/dpdp-act-skills.git

# Copy the skills into Claude's skill directory
mkdir -p ~/.claude/skills
cp -r dpdp-act-skills/skills/* ~/.claude/skills/
```

### Option B: Project-Level Installation
To equip an existing project workspace with DPDP Act compliance capabilities:

```bash
cd your-project
mkdir -p .claude/skills
cp -r /path/to/dpdp-act-skills/skills/* .claude/skills/
```

---

## 2. Invocation in Claude Code

Once installed, Claude Code automatically discovers the skills based on prompt intent and skill descriptions. You can also explicitly trigger them:

### Prompt Examples:
- **Router / Applicability**:
  > "Claude, evaluate whether our Singapore-hosted SaaS offering B2B subscriptions to Indian enterprises falls within Section 3 of the DPDP Act."
- **Consent & Notice**:
  > "Review our onboarding sign-up flow against Section 6 of the DPDP Act and Rule 3 of the DPDP Rules 2025. Does bundling email marketing violate the Act?"
- **Fiduciary Duties & Breaches**:
  > "A misconfigured database exposed 50,000 user records. What are our statutory notification obligations under Section 8(6) and Rule 7?"
- **Data Subject Rights**:
  > "A user requested immediate erasure of all account history, but tax laws require 7-year invoice retention. How do we balance Section 12(3) with Section 8(7)?"
- **Penalties & Cross-Border**:
  > "Can we transfer customer analytics data to Ireland? What is the penalty exposure under the DPDP Act Schedule for failure of reasonable security safeguards?"

---

## 3. Recommended `CLAUDE.md` Snippet

Add this snippet to your project's `CLAUDE.md` to enforce the statutory answering framework:

```markdown
## DPDP Act Compliance Guidelines
- When analyzing Indian data privacy matters, always consult the `skills/dpdp-*` skills.
- Structure all answers using the 8-point statutory framework: (1) Provision, (2) Plain interpretation, (3) DPDP Rule, (4) Commencement status, (5) Compliance implications, (6) Exceptions, (7) Official source, (8) Interpretive limitations.
- Note the phased enforcement timeline: Phase 1 (13 Nov 2025), Phase 2 (13 Nov 2026), and Phase 3 (13 May 2027). Never present future Phase 3 requirements as already enforceable statutory mandates.
```

