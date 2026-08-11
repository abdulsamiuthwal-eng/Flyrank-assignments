# FL-09 Video Script — ResearchScout Agent
**Abdul Sami Uthwal | FlyRank General AI Fluency | Target: 3–4 minutes**

---

## Shuru Karne Se Pehle (Recording Se Bahar)
- Flask server pehle se start hona chahiye: `python work/agent/web_app.py`
- Browser mein `http://127.0.0.1:5000` khula hona chahiye
- OBS ya Loom ON karo — phir neeche se shuru karo

---

## 🎬 SCRIPT START

---

### PART 1 — Intro

🟡 **KARO:** VS Code kholo jahan `FlyRank_Portfolio` folder sidebar mein dikh raha ho. Camera pe screen dikhao.

🎙️ **BOLO:**
> "Hi, I'm Abdul Sami Uthwal, FlyRank General AI Fluency intern.
> This is ResearchScout — an autonomous AI agent.
> You give it any arXiv paper ID, it fetches the paper live from the internet,
> generates a structured engineering research brief, and saves it to disk —
> all in under 2 seconds. Let me show you a live run right now."

---

### PART 2 — Web UI Dikhao

🟡 **KARO:** Browser pe switch karo jahan `http://127.0.0.1:5000` khula hai.

🎙️ **BOLO:**
> "This is the web interface. At the top you can see the 4-step agent pipeline —
> arXiv API fetch, XML parsing, synthesis, and filesystem save.
> I'll use one of these quick-select chips to load a paper."

🟡 **KARO:** Green chip `2312.00752 — Mamba SSM` pe click karo. Input box mein ID fill ho jayegi.

🎙️ **BOLO:**
> "I've selected arXiv paper 2312.00752 — that's the Mamba paper on
> linear-time sequence modeling. Now I'll run the agent."

---

### PART 3 — Live Run (Sabse Zaroori Part)

🟡 **KARO:** Bada wala **"Run Agent"** button click karo. Kuch mat bolo — pipeline animate hone do.

🎙️ **BOLO (jab steps light up ho rahey hon):**
> "You can see the pipeline steps activating in real time —
> first the arXiv REST API is being called live over the internet,
> then the XML response is being parsed,
> then the brief is being synthesised,
> and finally it's being written to the local filesystem."

🟡 **KARO:** Output brief neeche render ho jaye to elapsed time aur "saved" notice pe cursor le jao.

🎙️ **BOLO:**
> "Done. In under 900 milliseconds — live internet call, parse, synthesise, save.
> The full 5-section engineering brief is rendered here,
> and it's been automatically persisted to disk."

---

### PART 4 — Design Decision (FL-09 Requirement ✅)

🟡 **KARO:** Same browser screen pe raho. Koi click nahi karna.

🎙️ **BOLO:**
> "I want to explain one key design decision I made.
> Originally I tried downloading and parsing the full PDF of each paper.
> It worked — but it took 15 to 25 seconds per paper. That's completely unusable.
> So I switched to arXiv's Atom XML API feed instead.
> It's a tiny structured payload — arrives in milliseconds.
> That one decision dropped execution time from 18 seconds to under 2.
> A 12x speedup. Full PDF parsing is on the version 3 roadmap."

---

### PART 5 — Limitation (FL-09 Requirement ✅)

🟡 **KARO:** Brief ke andar Architecture section pe scroll karo aur cursor rakhho.

🎙️ **BOLO:**
> "Now for an honest limitation.
> Sections 2 through 4 of the brief — Architecture, Benchmarks, and Gotchas —
> are generated from a fixed engineering template.
> They don't dynamically extract content from the actual paper body.
> For papers outside machine learning or systems research,
> those sections may be too generic.
> The fix would be a domain classifier that picks the right template automatically.
> That's planned for version 3."

---

### PART 6 — CLI Run + End

🟡 **KARO:** VS Code terminal pe switch karo. Ye command type karo:
```
python work/agent/research_scout.py 1706.03762
```
Enter dabaao. Output scroll hone do.

🎙️ **BOLO:**
> "The agent also runs fully from the command line with zero dependencies.
> That was the Attention Is All You Need paper — executed and saved in seconds."

🟡 **KARO:** Terminal mein `[AGENT] EXECUTION COMPLETE` line pe cursor le jao.

🎙️ **BOLO:**
> "The full README with setup instructions, architecture diagram,
> evaluation results, and all documented limitations is in the repository root.
> Thank you for reviewing."

🟡 **KARO:** Recording BAND karo. ✅

---

## Post-Recording Check
- [ ] Video **3:00 – 5:00 minutes** ke beech hai?
- [ ] Live run dikh raha hai? (koi slides nahi)
- [ ] Design Decision bola? ✅
- [ ] Limitation boli? ✅
- [ ] YouTube par **Unlisted** upload karo → link copy karo → `fl09_submission.md` mein paste karo
