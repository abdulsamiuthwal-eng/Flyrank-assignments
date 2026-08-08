# FlyRank Internship Master Project & Chat Log — ABDUL SAMI UTHWAL

**Student Name:** ABDUL SAMI UTHWAL  
**Track:** FlyRank General AI Fluency / ML Track  
**GitHub Account:** [abdulsamiuthwal-eng](https://github.com/abdulsamiuthwal-eng)  
**Repository:** [Flyrank-assignments](https://github.com/abdulsamiuthwal-eng/Flyrank-assignments)  
**Live Portfolio Website:** [https://abdulsamiuthwal-portfolio.vercel.app/](https://abdulsamiuthwal-portfolio.vercel.app/)  

---

## 📌 How to Resume in Antigravity (Next Session Prompt)
Jab bhi aap Antigravity kholain aur naye session mein kaam shuru karna ho, bas AI ko yeh prompt dein:

> **"Read CHAT_HISTORY_GUIDE.md in my workspace and guide me on what to do next."**

---

## 🔗 Quick Reference Links & Deliverables

### 1. Live Web & Repository URLs
- **Live Portfolio (Vercel):** `https://abdulsamiuthwal-portfolio.vercel.app/`
- **GitHub Repository (Root):** `https://github.com/abdulsamiuthwal-eng/Flyrank-assignments`
- **Personal Agent Script:** `https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/agent/research_scout.py`
- **Week 7 Notebook:** `https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/notebooks/w07_action_playbook.ipynb`
- **Week 7 Stats JSON:** `https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/outputs/w07_playbook_stats.json`

### 2. Local Project File Paths
- **Project Root:** `c:\Users\abdul\Desktop\FlyRank_Portfolio\`
- **Portfolio HTML/CSS/JS:** `index.html`, `styles.css`, `app.js`
- **Personal Agent (ResearchScout):** `work/agent/research_scout.py`
- **Capstone HTML Report (PDF printable):** `work/outputs/capstone_submission.html`
- **Week 5 Model Notebook:** `work/notebooks/w05_baseline_model.ipynb`
- **Week 6 Audit Notebook:** `work/notebooks/w06_validation_audit.ipynb`
- **Week 7 Action Playbook Notebook:** `work/notebooks/w07_action_playbook.ipynb`

---

## 📜 Complete Progress Summary (Weeks 1 – 7)

### Week 1 – 4: Foundations & ML Signal Framing
- **CTR Opportunity Scoring Signal:** Structured CTR gap (`expected_ctr - actual_ctr`) across 600 synthetic search landing pages & 15 domain clusters.
- **Data Contract:** Defined schema for historical impressions, positions, word counts, and update frequency.

### Week 5: Baseline & Model Exploration
- Built & compared 5 baseline/ML models:
  - Baseline Rule F1: `0.480`
  - Logistic Regression F1: `0.273`
  - Decision Tree F1: `0.583`
  - Random Forest F1: `0.609`
  - **Gradient Boosting (Champion) F1:** `0.759` (ROC-AUC: `0.983`)

### Week 6: Validation Audit & Deliverables
- **Validation Audit:** Evaluated model under GroupKFold (domain-grouped split) to prevent data leakage. Validated F1 score: `0.783`.
- **Personal Agent (`ResearchScout`):** Built autonomous Python script (`work/agent/research_scout.py`) querying arXiv REST API, parsing Atom XML, and outputting structured Markdown briefs without external dependencies.
- **Personal Brand Portfolio:** Built HTML/CSS/JS site with Emerald & Amber aesthetic, deployed live to Vercel.
- **Week 6 Capstone Report:** Generated 4-page HTML report (`capstone_submission.html`) formatted for PDF export.

### Week 7: Content Action Playbook
- **Notebook:** Created and executed `work/notebooks/w07_action_playbook.ipynb`.
- **Key Sections:**
  1. **Ranked Queue & Reason Codes:** 3-tier system (`PRIORITY_REVIEW`, `SCHEDULED_WATCH`, `MONITOR_ONLY`) with machine-generated codes (e.g. `HIGH_IMPRESSION_VOLUME | LARGE_CTR_GAP`).
  2. **Archetype Mapping:** 5 content archetypes (Quick Win, Stale Authority, Thin Opportunity, Position Climber, Low Signal).
  3. **Decay & Refresh Insight:** Freshness bucket analysis (`Fresh`, `Recent`, `Aging`, `Stale`).
  4. **Limits & No-Go Cases:** 6 explicit human-review gates (no homepage automation, no low impression pages <200, no fresh content <30d, no E-A-T pages).
  5. **Cost/Value & Retrain Triggers:** Estimated editor time per tier + 4 retrain triggers (F1 < 0.72, Precision < 0.65, 40% drift, 90-day staleness).
  6. **Exports:** Exported `action_queue.csv` (gitignored), `w07_playbook_stats.json` (committed), and 2 figures (`w07_tier_distribution.png`, `w07_archetype_decay.png`).

---

## 📋 Submission Templates (Copy-Paste Ready)

### A. Week 6 Capstone Submission
- **Deliverable Links Box:**
  ```text
  https://abdulsamiuthwal-portfolio.vercel.app/
  https://github.com/abdulsamiuthwal-eng/Flyrank-assignments
  https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/agent/research_scout.py
  ```
- **Files to upload:** Export `work/outputs/capstone_submission.html` as PDF and upload it.

### B. Week 7 Action Playbook Submission
- **Deliverable Links Box:**
  ```text
  https://github.com/abdulsamiuthwal-eng/Flyrank-assignments
  https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/notebooks/w07_action_playbook.ipynb
  https://github.com/abdulsamiuthwal-eng/Flyrank-assignments/blob/main/work/outputs/w07_playbook_stats.json
  ```
- **Notes Box:** Copy notes from `work/outputs/w07_playbook_stats.json` or Week 7 chat logs.

---

## 🚀 Next Milestone: Week 8 Final Capstone Paper

In Week 8, you will deploy your final research paper. The paper will synthesize all work from Week 2 to Week 7 into a single live web page containing:
1. Title & Abstract (5 sentences)
2. Introduction & Problem Statement
3. Data Description (Public-safe framing)
4. Methodology (Features, Gradient Boosting model, GroupKFold split)
5. Results & Charts (Reusing figures from `work/figures/`)
6. Limitations & Honest Framing
7. Ranked Recommendations (Action Playbook from Week 7)
8. Reproducibility & Code Links
9. Data Credit & Link to `https://flyrank.ai`

*Last Updated & Saved by Antigravity Agent.*
