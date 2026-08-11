# FlyRank AI Systems & Machine Learning Portfolio
### End-to-End AI Engineering, Autonomous Literature Research Agent & Search Optimization

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20UI-000000?style=flat-square&logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Gradient%20Boosting-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-HTTPS%20Deployment-000000?style=flat-square&logo=vercel)
![arXiv](https://img.shields.io/badge/arXiv-Live%20API-B31B1B?style=flat-square)
![FlyRank](https://img.shields.io/badge/FlyRank-ML%20%26%20AI%20Fluency-059669?style=flat-square)

---

## 📌 Executive Overview

This repository represents the complete, production-verified portfolio of **Abdul Sami Uthwal** for the **FlyRank Internship (Machine Learning & General AI Fluency Tracks)**.

It combines three production-grade AI systems:
1. **Machine Learning CTR Opportunity Engine:** A GroupKFold domain-validated Gradient Boosting Classifier (**F1: 0.783, ROC-AUC: 0.983**) predicting search ranking engagement gaps across 600 landing pages.
2. **ResearchScout Autonomous Agent:** An autonomous literature research agent that queries the live arXiv REST API, parses Atom XML, synthesises 5-section engineering briefs, and saves Markdown files in under 900ms.
3. **Production Web Infrastructure:** A claim-first portfolio deployed on Vercel (`https://abdulsamiuthwal-portfolio.vercel.app/`) over HTTPS with Vercel Web Analytics, serverless Web3Forms lead capture, 98/100 PageSpeed score, and the official FlyRank Verified Graduate Badge.

---

## 📐 End-to-End System Architecture

```
                                 [USER INTERFACE LAYER]
                    ┌──────────────────────────────────────────────┐
                    │ Production Vercel Portfolio & Web UI         │
                    │ https://abdulsamiuthwal-portfolio.vercel.app/ │
                    └──────────────────────┬───────────────────────┘
                                           │
                        ┌──────────────────┴──────────────────┐
                        ▼                                     ▼
         ┌──────────────────────────────┐    ┌──────────────────────────────┐
         │ SYSTEM 1: ML RANKING ENGINE  │    │ SYSTEM 2: RESEARCH SCOUT AGENT│
         │ (sklearn Gradient Boosting)  │    │ (Python + arXiv REST API)    │
         └──────────────┬───────────────┘    └──────────────┬───────────────┘
                        │                                   │
                        ▼                                   ▼
         ┌──────────────────────────────┐    ┌──────────────────────────────┐
         │ GroupKFold Validation Audit  │    │ Atom XML Parser Engine       │
         │ F1: 0.783 | ROC-AUC: 0.983   │    │ xml.etree.ElementTree        │
         └──────────────┬───────────────┘    └──────────────┬───────────────┘
                        │                                   │
                        ▼                                   ▼
         ┌──────────────────────────────┐    ┌──────────────────────────────┐
         │ Tiered Action Playbook       │    │ Local Filesystem Persistence │
         │ (Protect / Rewrite / Merge) │    │ work/outputs/research_briefs │
         └──────────────────────────────┘    └──────────────────────────────┘
```

---

## 🗓️ 10-Week Engineering Journey (Start to Finish)

### Phase 1: Search Ranking CTR Signal Framing (Weeks 1–4)
- **Problem Statement:** Raw search rank alone fails to predict user engagement. Visible pages often under-capture clicks due to poor snippet metadata.
- **Signal Formulation:** Formulated the CTR Opportunity gap signal:
  $$\text{CTR\_Opportunity} = \text{Expected\_CTR}(\text{Position}) - \text{Actual\_CTR}$$
- **Data Contract:** Processed 600 synthetic landing pages across 15 domain clusters with zero future-window data leakage.

### Phase 2: ML Model Benchmarking & GroupKFold Validation (Weeks 5–6)
- **Validation Design:** Implemented domain-grouped `GroupKFold (k=5)` cross-validation to prevent cluster leakage across folds.
- **Model Progression:**
  - *Rule Baseline:* F1 = 0.480
  - *Logistic Regression:* F1 = 0.273 | ROC-AUC = 0.612
  - *Decision Trees:* F1 = 0.583 | ROC-AUC = 0.741
  - *Random Forest:* F1 = 0.609 | ROC-AUC = 0.812
  - **Champion Gradient Boosting:** **F1 = 0.783 | ROC-AUC = 0.983** (+63.1% lift over baseline).
- **Action Engine:** Mapped predictions into a 4-tier Content Action Playbook (Tier 1 Protect → Tier 4 Prune/Merge).

### Phase 3: Autonomous Agent & Live Lead Capture (Weeks 7–8)
- **ResearchScout Agent (`work/agent/research_scout.py`):** Autonomous agent consuming arXiv paper IDs / topic keywords, parsing Atom XML via standard library, and generating structured 5-section briefs.
- **Flask Web Server (`work/agent/web_app.py`):** Flask REST API serving an Emerald & Amber Web UI at `http://127.0.0.1:5000`.
- **Live Lead Capture Engine:** Serverless Web3Forms integration delivering client leads directly to Gmail from the production site.

### Phase 4: Hardening, Launch, Analytics & Capstone (Weeks 9–10)
- **Break Your Own Site Hardening:** Form debouncing, input `.trim()` sanitization, RFC email regex validation, and PageSpeed audit (**98 / 100**).
- **Plant Your Flag Launch:** OpenGraph social cards, Twitter summary cards, SVG favicon, Vercel Web Analytics, and embedded FlyRank Verified Graduate Badge.
- **Capstone Deliverables:** Deployed 10-page Research Paper (`https://abdulsamiuthwal-portfolio.vercel.app/work/paper/index.html`) and live video demo (`https://youtu.be/-uCqi_JDjfY`).

---

## ⚡ Quickstart — Running the Systems

### 1. Run ResearchScout Agent (CLI Mode — Zero External Dependencies)
```bash
# Clone the repository
git clone https://github.com/abdulsamiuthwal-eng/Flyrank-assignments.git
cd Flyrank-assignments

# Query a paper by arXiv ID
python work/agent/research_scout.py 2312.00752

# Query by topic keyword
python work/agent/research_scout.py "attention mechanism transformer"
```

### 2. Run ResearchScout Web UI (Flask Server)
```bash
# Install Flask (only dependency)
pip install flask

# Start the Flask web app
python work/agent/web_app.py
```
Open browser at: `http://127.0.0.1:5000`

---

## 📊 Empirical Benchmark Results

| System / Model | Metric | Result | Benchmark Status |
|---|---|---|---|
| **Champion Gradient Boosting** | GroupKFold Validated F1 | **0.783** | ✅ Champion |
| **Champion Gradient Boosting** | ROC-AUC | **0.983** | ✅ Champion |
| **Rule-Based Baseline** | GroupKFold Validated F1 | **0.480** | Baseline |
| **ResearchScout Agent** | End-to-End Execution Latency | **< 900ms** | ✅ Sub-2s Target |
| **Portfolio Performance** | Lighthouse PageSpeed | **98 / 100** | ✅ Production Ready |
| **First Contentful Paint (FCP)** | Navigation Timing API | **0.4s** | ✅ Sub-second |

---

## 🛠️ Key Design Decisions & Known Limitations

### Design Decision: Atom XML API vs. Full PDF Parsing
- **Trade-off:** Initial prototypes downloaded and parsed full paper PDFs via `pdfplumber`, taking 15–25 seconds per paper.
- **Decision:** Switched to arXiv's native Atom XML REST API feed, returning sub-kilobyte metadata.
- **Result:** Execution time dropped from **~18s → ~1.4s** (a **12× speedup**).

### Documented Limitations
1. **Abstract-Based Template Synthesis:** Sections 2–4 of ResearchScout briefs use a structured engineering template based on the abstract rather than full PDF body extraction.
2. **arXiv API Rate Limits:** Public arXiv REST API enforces informal rate limits (~3 req/sec); exponential back-off handling is documented.

---

## 📁 Repository Directory Structure

```
Flyrank-assignments/
├── README.md                            # Comprehensive master documentation
├── index.html                           # Production Vercel portfolio with SEO & badge
├── styles.css                           # Design tokens & responsive styles
├── app.js                              # Hardened contact form handler & debouncing
├── generate_pdf.py                      # Playwright PDF compilation engine
├── submission/                          # Submission artifacts & verification files
│   ├── paper_url.txt                    # Mandatory Capstone deployed paper link
│   ├── fl09_submission.md               # FL-09 portal notes & video script
│   ├── w08_make_it_do_something_submission.*
│   ├── w09_break_your_own_site_report.*
│   ├── w09_plant_your_flag_submission.*
│   ├── w09_the_plan_to_keep_building_submission.*
│   └── w10_send_the_link_capstone_submission.*
└── work/
    ├── agent/                           # ResearchScout Agent & Web UI
    │   ├── research_scout.py            # Core agent class (CLI entry point)
    │   ├── web_app.py                   # Flask REST server
    │   └── templates/index.html         # Premium Emerald & Amber Web UI
    ├── notebooks/                       # Reproducible Jupyter Notebooks
    │   ├── w02_ml_task_framing.ipynb
    │   ├── w03_data_contract.ipynb
    │   ├── w04_baseline_score.ipynb
    │   ├── w05_model.ipynb
    │   ├── w06_validation_audit.ipynb
    │   ├── w07_action_playbook.ipynb
    │   └── capstone.ipynb
    ├── paper/                           # Deployed 10-page Research Paper
    │   └── index.html
    └── outputs/                         # Model metrics, briefs & figures
```

---

## 🔬 Reproducibility & Data Credit

- **Notebook Execution:** All machine learning experiments, feature engineering pipelines, and validation audits are fully reproducible via the notebooks in `work/notebooks/`.
- **Data Source Credit:** *"Built on the FlyRank ML Internship dataset"* — Data source credited to [FlyRank](https://flyrank.ai).

---

## 👤 Author

**Abdul Sami Uthwal**  
FlyRank Intern — Machine Learning & General AI Fluency Tracks  
GitHub: [@abdulsamiuthwal-eng](https://github.com/abdulsamiuthwal-eng)  
Portfolio: [abdulsamiuthwal-portfolio.vercel.app](https://abdulsamiuthwal-portfolio.vercel.app)
