# Gemini CLI Integration Guide

This guide explains how to use the **DPDP Act 2023 & Rules 2025** skills suite with the **Google Gemini CLI** or Google GenAI SDK scripts.

---

## 1. Directory Setup

Clone or place the skills into your working directory or prompt library:

```bash
git clone https://github.com/theruturaj/dpdp-act-skills.git
```

---

## 2. Using System Instructions with Gemini CLI

When launching interactive sessions with `gemini` or executing automated checks, inject the router and skills as system instructions or context files:

```bash
# Example query injecting the overview and specific skill
gemini --system-instruction "$(cat dpdp-act-skills/skills/dpdp-act-overview/SKILL.md)" \
  "What are the mandatory items in a privacy notice under Section 5 and Rule 3?"
```

---

## 3. Python Automation Example using `google-genai`

```python
import os
from google import genai

client = genai.Client()

# Load canonical skill contents
with open("skills/dpdp-act-overview/SKILL.md") as f:
    overview_skill = f.read()
with open("skills/dpdp-fiduciary-obligations/SKILL.md") as f:
    fiduciary_skill = f.read()

system_prompt = f"""
You are an expert Indian data privacy counsel.
Ground all responses in the following verified statutory knowledge:
{overview_skill}

{fiduciary_skill}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain our obligations under Section 8(5) and Rule 6 if user passwords were leaked in plain text.",
    config={"system_instruction": system_prompt}
)

print(response.text)
```
