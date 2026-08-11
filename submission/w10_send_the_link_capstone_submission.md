# Week 10 Capstone Deliverable: Send the Link — Launch, Demo & Story

**Track:** General AI Fluency  
**Student:** Abdul Sami Uthwal  
**Live Launch URL:** `https://abdulsamiuthwal-portfolio.vercel.app/`  
**Live Demo Video URL:** `https://youtu.be/-uCqi_JDjfY`  
**GitHub Repository:** `https://github.com/abdulsamiuthwal-eng/Flyrank-assignments`  
**Submission Date:** 2026-08-12  

---

## 1. Executive Summary & Capstone Vision

> *"A portfolio is not a static PDF or a classroom assignment—it is a live, verifiable career platform that proves what you can build, deploy, and defend."*

This final Capstone deliverable synthesises the three core pillars of the FlyRank General AI Fluency Track:
1. **The Launch:** Public deployment of a claim-first AI systems portfolio over HTTPS on Vercel, fortified with live web analytics, social OpenGraph cards, and the FlyRank Verified Graduate Badge.
2. **The Demo:** Video proof (`https://youtu.be/-uCqi_JDjfY`) demonstrating live end-to-end autonomous agent execution, API response latency, and verbal explanation of design decisions and limitations.
3. **The Story:** The complete 10-week engineering journey from heuristic CTR opportunity scoring to champion gradient boosting models, autonomous literature research agents, serverless lead capture pipelines, and production site hardening.

---

## 2. Pillar 1: The Launch (Production Infrastructure)

- **Production Domain:** `https://abdulsamiuthwal-portfolio.vercel.app/`
- **Security & Protocol:** HTTPS with automated TLS/SSL certificate via Vercel Edge Network.
- **Analytics & Tracking:** Vercel Insights & Speed Analytics script (`/_vercel/insights/script.js`) active in `<head>`.
- **Launch Hygiene:**
  - Custom SVG Lightning Favicon (`data:image/svg+xml...`)
  - OpenGraph cards (`og:title`, `og:description`, `og:image`, `og:url`)
  - Twitter Summary Cards (`summary_large_image`)
  - Schema.org `Person` JSON-LD structured data
- **FlyRank Credential Badge:** Interactive FlyRank Verified Graduate Badge embedded in website footer linking to `https://internship.flyrank.ai`.

---

## 3. Pillar 2: The Demo (Video Proof & Agent Architecture)

- **Demo Video URL:** `https://youtu.be/-uCqi_JDjfY` (Unlisted YouTube)
- **Agent Name:** `ResearchScout` Autonomous AI/ML Literature Research Agent
- **Core Architecture:**
  1. **Tool 1 (arXiv REST API):** Connects live to `export.arxiv.org/api/query` and fetches Atom XML payloads.
  2. **XML Parser:** Standard library `xml.etree.ElementTree` namespace-aware parsing.
  3. **Core Job:** Synthesises a structured 5-section engineering research brief (Executive Summary, Technical Architecture, Empirical Benchmarks, Implementation Gotchas, Evaluation Receipt).
  4. **Tool 2 (Filesystem Storage):** Persists generated Markdown briefs to `work/outputs/research_briefs/`.
- **Execution Performance:** End-to-end runtime of **681ms - 898ms** (<2 seconds target).
- **Verbal Explanations On Camera:**
  - **Design Decision:** Switched from full PDF parsing (`pdfplumber`) to Atom XML API feed for a **12× latency speedup** (18s → 1.4s).
  - **Known Limitation:** Sections 2–4 use a fixed engineering template based on the abstract, rather than full-text PDF extraction (v3 roadmap enhancement).

---

## 4. Pillar 3: The Story (10-Week Engineering Journey)

```
┌────────────────────────────────────────────────────────────────────────┐
│  WEEKS 1–4: Signal Framing & Data Contract                             │
│  Engineered CTR opportunity scoring signal (expected - actual CTR)     │
│  across 600 landing pages & 15 domain clusters.                        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  WEEKS 5–6: ML Modeling & GroupKFold Validation Audit                  │
│  Benchmarked 5 models; Champion Gradient Boosting achieved F1: 0.783   │
│  and ROC-AUC: 0.983 under domain-grouped zero-leakage split.           │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  WEEKS 7–8: Autonomous Agent & Live Lead Capture System                │
│  Built ResearchScout Python agent + wired Web3Forms API to production  │
│  Vercel portfolio for real-time lead delivery to Gmail.                │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  WEEKS 9–10: Hardening, Launch, Analytics & Graduate Badge             │
│  Hardened form debouncing, injected SEO/OpenGraph, PageSpeed 98/100,   │
│  and installed FlyRank Verified Graduate Badge in footer.              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Preserved Build Context & Future Roadmap

The entire codebase, design tokens (`#059669` Emerald & `#d97706` Amber), typography, and student profile remain 100% active and tracked in workspace configuration files:

- **`CHAT_HISTORY_GUIDE.md`:** Master trajectory log of all 10 weeks of FlyRank deliverables.
- **`.agents/AGENTS.md`:** Persistent workspace rules and mandatory submission templates.
- **`README.md`:** Comprehensive reproduction guide for external reviewers and employers.

Future case study additions follow the 3-beat protocol (Problem -> Architecture -> ROI), enabling zero-overhead project expansions in minutes.

---

## 6. Capstone Evaluation Criteria Pass/Revise Self-Check

- [x] **Live portfolio URL submitted:** `https://abdulsamiuthwal-portfolio.vercel.app/`
- [x] **Demo video link submitted:** `https://youtu.be/-uCqi_JDjfY`
- [x] **Story breakdown provided:** Complete 10-week narrative documented
- [x] **Proof of launch verified:** Live HTTPS, Vercel Web Analytics, OpenGraph social card, and FlyRank Graduate Badge verified
