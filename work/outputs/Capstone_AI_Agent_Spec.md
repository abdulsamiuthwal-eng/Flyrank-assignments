# Capstone AI Agent Design Specification
**Project:** FlyRank ResearchScout & Intelligence Agent  
**Phase:** Build (Core) | **Estimated Build Hours:** 10 Hours  
**Author:** Abdul Sami | **Track:** AI Systems & Automation Engineering  

---

## 1. Job to be Done & Scope
- **Agent Name:** `ResearchScout Agent`
- **Primary Job:** An autonomous research assistant that monitors AI/ML literature (arXiv, PapersWithCode), extracts methodology frameworks, synthesizes papers into structured markdown briefs, and highlights implementation gotchas for engineering sprints.
- **Target User & Usage:** Single-user (ML Engineer/Student). Used daily for automated paper digests and on-demand for specific arXiv ID deep dives.
- **Build Scope (10 Hours):**
  - Hours 1-3: Setup arXiv/PDF ingestion pipeline & schema parser.
  - Hours 4-6: Build LLM synthesis & tool-calling engine.
  - Hours 7-8: Implement guardrails, error handling, and 5 pre-build eval cases.
  - Hours 9-10: CLI interface & end-to-end evaluation runs.

---

## 2. Tools, Data Sources & Access Plan
1. **arXiv REST API:** Public REST API for querying papers by ID/topic (Free, no API key needed).
2. **PyPDF2 / PDFPlumber:** Local Python PDF text extraction tool.
3. **Gemini 2.5/3 API:** LLM inference & function calling engine (Free tier via API key).
4. **Local Markdown Store:** Local file system (`work/outputs/research_briefs/`) for persistent report storage.

---

## 3. Draft System Instructions (Prompt)
```text
You are ResearchScout, an expert AI research assistant. Your sole role is to ingest technical AI papers and produce rigorous, hallucination-free engineering briefs.

Strict Operational Guidelines:
1. Always ground your analysis strictly in the provided paper text.
2. Structure output into: (A) Key Innovation, (B) Architecture Breakdown, (C) Empirical Results, and (D) Implementation Gotchas.
3. Never fabricate benchmark metrics or cite unverified claims.
4. If a PDF scan is unreadable or missing sections, explicitly declare missing data.
```

---

## 4. Five Pre-Build Eval Cases
| ID | Test Scenario | Input Prompt / Trigger | Expected Output / Success Criteria |
|:---|:---|:---|:---|
| **E1** | Specific arXiv ID Lookup | `analyze_paper("2312.00752")` | Extracts Mamba architecture details, compares state-space model vs Transformer attention. |
| **E2** | Topic Synthesis | `search_topic("LoRA fine-tuning efficiency")` | Returns top 3 papers sorted by relevance, with consolidated comparison table. |
| **E3** | Out-of-Domain Refusal | "Write a marketing cold email" | Refuses politely and redirects user to research capabilities. |
| **E4** | Corrupted PDF Fallback | Invalid/corrupted PDF link | Triggers error handler gracefully without crash; returns clear error log. |
| **E5** | Math Formula Extraction | Paper with heavy LaTeX equations | Extracts core equations and translates them into plain-English intuition. |

---

## 5. Risks & Guardrails
- **Risks Identified:** Hallucinated benchmarks, execution of untrusted paper code snippets, accidental file overwrites.
- **Must Confirm:** Must prompt for user confirmation before overwriting existing research briefs or executing external shell commands.
- **Must Never Do:** Never execute unverified python code snippets found in papers; never modify environment configuration files.

---

## 6. Platform Choice & Justification
- **Chosen Platform:** Custom Python Scripted Agent (Python + Gemini SDK + LangChain Tools).
- **Alternative Evaluated:** Claude Cowork / Custom GPTs (Paid platforms).
- **Justification:** Python scripted agent is 100% free, runs locally with full access to filesystem and arXiv APIs, provides complete control over evaluation harnesses, and avoids vendor lock-in.
