# Handover — DSC4043 Group Project

**From:** Aliff
**To:** Yasierul, Amir, Ramzi
**Your deadline:** Friday 26 September, 9:00pm

---

## Read this first

The dataset is downloaded, merged, cleaned and exported. **You do not need to touch the raw data.** Your script already loads the clean file for you — just fill in the blanks marked `# TODO`.

Three rules, and the whole project depends on them:

1. **Do not re-clean the data.** `data/clean/student_clean.csv` is the only version anyone uses. If you think something is wrong with it, message me — don't fix it yourself, or our report will contain four different row counts.
2. **There is no column called `G3`.** After the merge it's `G3_mat` (Mathematics) or `G3_por` (Portuguese). Same for `absences`, `studytime`, `failures` and most others. Open `docs/data_dictionary.md` — every column is listed with its meaning and range.
3. **Every plot needs 2–3 sentences of interpretation.** The rubric gives up to 20 marks for visualisation but caps at 10 for "few plots, weak explanation". Your script has an `INTERPRETATION` string under each plot. Fill it in. This is where the marks actually are.

---

## Setup (5 minutes)

```bash
git clone <repo-url>
cd DSC4043-group-project

python3 -m venv .venv          # Windows: py -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

python src/0X_your_file.py     # should run with no errors before you write anything
```

**If you get `command not found: pip` on a Mac — that is normal.** Plain `pip` does not exist there; it is `pip3`. The virtual environment above provides `pip`, so just make sure you ran the `source .venv/bin/activate` line first. Your prompt shows `(.venv)` when it worked. Do not run `pip3 install` without the venv — macOS usually blocks it with an `externally-managed-environment` error.

If the folder path has spaces in it, quote it: `cd "…/Group Project/DSC4043-group-project"`.

**In VS Code:** `Cmd+Shift+P` → **Python: Select Interpreter** → pick the one under `./.venv/bin/python`, so the Run button uses the packages you just installed.

Prefer Colab? Open `notebooks/DSC4043_master.ipynb`, set `REPO` in the first cell, and run. It pulls the data from GitHub — nothing to install, nothing to upload. **If setup fights you for more than ten minutes, switch to Colab and message me.** Do not lose an evening to environment problems; that is not what you are being marked on.

---

## Your assignments

### Yasierul → `src/02_eda_matplotlib.py`
Summary measures table + **4 Matplotlib plots**. ~12 of 60 marks.

1. Histogram — distribution of `G3_mat`
2. Bar chart — mean `G3_mat` by `studytime_mat`
3. Scatter — `absences_mat` vs `G3_mat` (the result is surprising; report it honestly)
4. Grouped bar — grade progression G1 → G2 → G3, both subjects

Also export `docs/summary_measures.csv` so it can be pasted into the report.

### Amir → `src/03_eda_seaborn.py`
**3 Seaborn plots** + the APA reference list. ~8 of 60 marks + references.

5. Correlation heatmap — **do this one first and tell Ramzi when it's done**, his section references it
6. Boxplot — `G3_mat` by `higher_mat` (the biggest gap in the dataset)
7. Countplot — grade band distribution, Mathematics vs Portuguese

The reference list is mostly written in your file. You need to add the UCI entry and check the DOI.

### Ramzi → `src/04_statistical_analysis.py`
Central tendency, dispersion, correlation, **and the case study**. 15 of 60 marks — the largest single block.

- Mean, median, mode across 6 key variables
- Range, variance, standard deviation, IQR, coefficient of variation
- Pearson *r* and *p* for 9 variable pairs
- **The case study — about one page.** Three options are described in your file. Option B (`G3_mat` vs `G3_por`) is recommended: 104 students pass Portuguese but fail Mathematics, against only 9 the other way. That asymmetry is the most interesting thing in the whole dataset.

### Aliff (me)
Introduction, Data Preparation & Cleaning, Discussion & Conclusion. Plus integration and the final PDF. I'm on call all week — if your script errors, message me, don't lose an evening to it.

---

## What "done" means

Before you tell me you've finished, all four must be true:

- [ ] Your script runs top to bottom with **no errors**, from a fresh terminal
- [ ] Your PNGs are in `figures/` and actually show data (not blank)
- [ ] Every `INTERPRETATION` string is written — the script prints `<-- STILL A TODO` for any you missed
- [ ] You've committed **only your own file** and pushed

---

## Timeline

| When | What |
|---|---|
| **Wed 24 Sep** | Everyone has cloned the repo and run their script once. Message the group if anything fails. |
| **Thu 25 Sep** | Plots drawn, interpretations in draft |
| **Fri 26 Sep, 9pm** | All three scripts done and pushed. Report sections sent to me. |
| **Sat 27 Sep** | I integrate everything and send the assembled draft for proofreading |
| **Sun 28 Sep** | Individual reflections due, final check, submit |

We have until 14 October, so finishing this week leaves a two-week buffer. That buffer is the point — don't spend it in advance.

---

## Your individual reflection (40 marks — graded individually)

This is worth almost as much as the entire group report, and it's marked per person. 1–2 pages each:

1. **Contribution (10)** — what you did, with evidence: code snippets, your figures, your specific role
2. **Challenges (10)** — at least one real technical or conceptual problem and how you solved it
3. **Learning & insights (10)** — what you learned about pandas, Matplotlib, Seaborn, statistics, and where it applies in the real world
4. **CLO reflection (10)** — link your work to *"Apply statistical and computational tools to applied data science problems"*

**Draft it on Friday while the work is fresh.** The "provide evidence" requirement is brutal to reconstruct a week later, and vague reflections score 1–5 instead of 6–10.

---

## Using AI help

Allowed? Check with the lecturer first - our brief says plagiarism will be
penalised and faculties treat AI assistance differently. If you do use it,
read **`docs/AI_HELP.md`** first. It has a prompt that keeps the AI from
breaking the dataset, and explains which parts you must write yourself
(short version: the INTERPRETATION text and your reflection).

## If you get stuck

Message the group. The whole reason the work is split this way is that your three scripts are completely independent — nothing you do can break anyone else's work, so there's no risk in experimenting. The only shared thing is the clean CSV, and that's read-only.
