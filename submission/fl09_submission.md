# FL-09 — FlyRank Portal Submission Notes

**Assignment Code:** FL-09  
**Track:** General AI Fluency  
**Week:** 8  
**Student:** Abdul Sami Uthwal  
**Submission Date:** 2026-08-11  

---

## Deliverable Links Box (Copy & Paste)

```text
https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/README.md
https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/agent/research_scout.py
https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/agent/web_app.py
https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/agent/templates/index.html
https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/submission/fl09_submission.md
https://youtu.be/-uCqi_JDjfY
```



---

## Notes Box (Copy & Paste)

```
# FL-09 Deliverable: Documentation and Demo Video
Student: Abdul Sami Uthwal
Track: General AI Fluency
Agent: ResearchScout — Autonomous AI/ML Literature Research Agent

---

## What the Agent Does
ResearchScout is an autonomous AI research agent that:
1. Accepts any arXiv paper ID or topic keyword as input.
2. Connects live to the arXiv REST API (export.arxiv.org/api/query) and fetches paper metadata.
3. Parses the Atom XML response using Python's standard xml.etree.ElementTree library.
4. Synthesises a structured 5-section engineering research brief (Executive Summary, Architecture, Benchmarks, Gotchas, Eval Receipt).
5. Persists the brief as a Markdown file to the local filesystem.
All executed in under 2 seconds with zero external dependencies (CLI mode).

---

## Deliverable 1: README
Location: README.md in repository root (https://github.com/abdulsamiuthwal-eng/Flyrank-assignments)
Sections included:
- Overview and target audience
- Full architecture diagram (ASCII flow)
- CLI setup and Web UI setup (dual run methods)
- Concrete usage examples with 4 benchmark papers
- v2 Evaluation results table (execution time, parse accuracy, write success rate)
- Design Decision: XML vs PDF parsing (12x speedup rationale)
- Known Limitations list (5 documented limitations)

---

## Deliverable 2: Demo Video
Duration: 3 to 5 minutes
Format: Screen recording with live narration
Content:
- Live Flask server startup and browser Web UI demonstration
- Live arXiv query: paper 2312.00752 (Mamba SSM)
- Pipeline steps animated in real-time in the UI
- Generated brief rendered and filesystem save confirmed
- CLI run: paper 1706.03762 (Attention Is All You Need)
- Design Decision explained on camera: Atom XML API vs full PDF parsing
- Limitation explained on camera: Template-based synthesis sections
Tool Used: OBS Studio / Loom (unlisted YouTube upload)

---

## Evaluation Criteria Self-Check
[x] A stranger could reproduce the setup from the README alone
[x] Eval results and limitations included, not hidden
[x] Video shows a live end-to-end run (no slides)
[x] Video runs 3 to 5 minutes with clear narration
[x] One design decision explained on camera (XML vs PDF)
[x] One limitation explained on camera (template-based synthesis)
```

---

## Files Box

Upload or link:
- `README.md` (in repository root)
- YouTube Unlisted Video Link

---

> **Remember:** After uploading your video to YouTube (Unlisted), paste the link into the Deliverable Links Box above and the Notes Box before submitting on the FlyRank portal.
