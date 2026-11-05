# Custom AI Agent Integration Guide

This guide details how to integrate the **DPDP Act 2023 & Rules 2025** skills into custom agent frameworks, including LangChain, LlamaIndex, AutoGen, CrewAI, and native OpenAI/Anthropic tool systems.

---

## 1. Design Architecture: Universal Agent Knowledge Injection

The skills in `skills/*/SKILL.md` are self-contained Markdown files with YAML frontmatter designed for:
1. **Dynamic Tool Calling / Retrieval**: An agent can inspect frontmatter descriptions to decide which skill to load into context.
2. **Context Injection**: The entire skill or relevant sections can be loaded into system instructions without platform-specific dependencies.
3. **Deterministic Citations**: All statutory citations are explicit, enabling the agent to cite exact Section and Rule numbers.

---

## 2. Dynamic Tool Calling Implementation (Python)

```python
import os
import glob
import re

class DPDPSkillRegistry:
    def __init__(self, skills_dir="skills"):
        self.skills = {}
        for path in glob.glob(f"{skills_dir}/*/SKILL.md"):
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
            if match:
                raw_frontmatter, body = match.groups()
                name = re.search(r"name:\s*(.+)", raw_frontmatter).group(1).strip()
                desc = re.search(r"description:\s*(.+)", raw_frontmatter).group(1).strip()
                self.skills[name] = {"description": desc, "content": body}

    def list_skills(self):
        return {name: data["description"] for name, data in self.skills.items()}

    def get_skill(self, skill_name: str) -> str:
        if skill_name in self.skills:
            return self.skills[skill_name]["content"]
        raise KeyError(f"Skill '{skill_name}' not found. Available: {list(self.skills.keys())}")

# Example: LangChain or OpenAI function definition
registry = DPDPSkillRegistry()

def lookup_dpdp_law(skill_name: str) -> str:
    """
    Retrieve authoritative DPDP Act 2023 and DPDP Rules 2025 legal knowledge.
    Options: 'dpdp-act-overview', 'dpdp-consent-and-notice', 'dpdp-fiduciary-obligations', 
             'dpdp-data-principal-rights', 'dpdp-board-enforcement'.
    """
    return registry.get_skill(skill_name)
```

---

## 3. RAG & Vector Indexing Strategy

If indexing skills into a Vector DB (e.g. Pinecone, Chroma, pgvector):
- **Chunking strategy**: Chunk by Markdown H2 (`##`) headers. Each H2 section (e.g. `## Grounds for Processing`, `## Notice Requirements`) is self-contained.
- **Metadata tagging**: Attach `statute: DPDP Act 2023`, `rules: DPDP Rules 2025`, and `phase: Phase 1/2/3` to each chunk.
- **Enforcement filtering**: Filter retrieval results based on client requirement (e.g., filter for currently in force provisions vs preparation for Phase 3).
