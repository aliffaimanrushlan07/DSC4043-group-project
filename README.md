# DSC4043 — Introduction to Data Science | Group Project

**Bachelor of Information Technology (Hons) in Computer Application Development**
Semester August 2026 · Submission deadline **14 October 2026, 5:00pm**

---

## Dataset

**Student Performance** — UCI Machine Learning Repository
**Source link:** https://archive.ics.uci.edu/dataset/320/student+performance

Two files covering secondary school students at two Portuguese schools:

| File | Subject | Records |
|------|---------|---------|
| `student-mat.csv` | Mathematics | 395 |
| `student-por.csv` | Portuguese | 649 |

These are merged on 13 student-identity attributes to give **382 students who took both subjects**, which is the analysis dataset for this project.

---

## Team and ownership

| Member | Responsibility | File | Report section |
|--------|----------------|------|----------------|
| **Aliff** | Data preparation, repo, integration | `src/01_data_prep.py` | Introduction · Data Preparation · Discussion & Conclusion |
| **Yasierul** | EDA — Matplotlib | `src/02_eda_matplotlib.py` | Summary measures + 4 plots |
| **Amir** | EDA — Seaborn | `src/03_eda_seaborn.py` | 3 plots + APA references |
| **Ramzi** | Statistical analysis | `src/04_statistical_analysis.py` | Statistical Analysis + case study |

**Rule: you commit to your own file only.** Nobody else's. This is what keeps the repo conflict-free.

---

## Repository layout

```
DSC4043-group-project/
├── data/
│   ├── raw/                    # original UCI files — never edit
│   │   ├── student-mat.csv
│   │   └── student-por.csv
│   └── clean/
│       ├── student_clean.csv       # THE analysis dataset (382 × 61)
│       └── merge_audit_outer.csv   # audit trail of excluded records
├── src/
│   ├── 01_data_prep.py             # Aliff
│   ├── 02_eda_matplotlib.py        # Yasierul
│   ├── 03_eda_seaborn.py           # Amir
│   ├── 04_statistical_analysis.py  # Ramzi
│   └── _make_data_dictionary.py    # utility, Aliff only
├── docs/
│   ├── data_dictionary.md          # READ THIS BEFORE CODING
│   └── HANDOVER.md                 # what each member does
├── figures/                        # exported PNGs, 300 dpi
└── notebooks/
    └── DSC4043_master.ipynb        # Colab notebook for submission
```

---

## Getting started

### 1. Clone and create a virtual environment

**macOS / Linux**

```bash
git clone <this-repo-url>
cd DSC4043-group-project

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows (PowerShell)**

```powershell
git clone <this-repo-url>
cd DSC4043-group-project

py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> **On macOS the command is `pip3`, not `pip`** — plain `pip` usually does not exist. Inside an activated virtual environment `pip` works normally, which is why the commands above use it. If you skip the venv and run `pip3 install` directly, macOS will often refuse with an `externally-managed-environment` error. The venv avoids both problems.

Your prompt shows `(.venv)` when the environment is active. Re-activate it in every new terminal with `source .venv/bin/activate`.

If the path to this folder contains spaces, wrap it in quotes: `cd "…/Group Project/DSC4043-group-project"`.

### 2. Point VS Code at the environment

`Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows) → **Python: Select Interpreter** → choose the one under `./.venv/bin/python`. The Run button and the notebook will then use the right packages. `.venv/` is already in `.gitignore`, so it will not be committed.

### 3. Run the scripts

```bash
python src/01_data_prep.py             # Aliff only — already run, output committed
python src/02_eda_matplotlib.py        # Yasierul
python src/03_eda_seaborn.py           # Amir
python src/04_statistical_analysis.py  # Ramzi
```

Scripts must be run from the repository root. They resolve their own paths, so you do not need to edit anything.

### Working in Google Colab

Open `notebooks/DSC4043_master.ipynb`. It pulls the clean data straight from this repository — no file uploads, no `drive.mount`, and nothing to install. If the virtual environment gives you trouble, just use Colab.

---

## The three rules

1. **Never re-clean the data.** `student_clean.csv` is the single source of truth. If you think something is wrong with it, tell Aliff — do not fix it in your own script, or the report will contain four contradictory row counts.
2. **Use the suffixed column names.** After the merge there is no plain `G3`. It is `G3_mat` or `G3_por`. Everything is listed in `docs/data_dictionary.md`.
3. **Every plot needs 2–3 sentences of interpretation.** The marking rubric awards up to 20 for visualisation but caps at 10 for "few plots, weak explanation". The explanation is where the marks are.

---

## Key findings so far

| Relationship | Pearson *r* | Reading |
|---|---|---|
| `G2_mat` → `G3_mat` | **+0.903** | Second-period grade nearly determines the final grade |
| `G1_mat` → `G3_mat` | +0.805 | Strong from the first period onward |
| `G3_mat` ↔ `G3_por` | **+0.480** | Same students, only moderately related across subjects |
| `failures_mat` → `G3_mat` | −0.381 | Strongest non-grade predictor |
| `Medu` → `G3_mat` | +0.205 | Mother's education has a weak positive effect |
| `studytime_mat` → `G3_mat` | +0.091 | Near-negligible — a finding worth discussing |
| `absences_mat` → `G3_mat` | +0.029 | No relationship at all, contrary to expectation |

Mathematics pass rate **66.8%** vs Portuguese **91.6%**. 104 students pass Portuguese but fail Mathematics; only 9 the reverse.

---

## Reference

Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student performance. In A. Brito & J. Teixeira (Eds.), *Proceedings of 5th FUture BUsiness TEChnology Conference* (pp. 5–12). EUROSIS.
