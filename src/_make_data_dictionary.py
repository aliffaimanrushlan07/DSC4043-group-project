"""
Utility (Aliff only): regenerates docs/data_dictionary.md from the actual
exported clean file, so dtypes and ranges are never out of date.
Run after any change to 01_data_prep.py.
"""
import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df = pd.read_csv(os.path.join(BASE, "data", "clean", "student_clean.csv"))

DESC = {
    # --- merge keys (13) ---
    "school": "School attended: GP = Gabriel Pereira, MS = Mousinho da Silveira",
    "sex": "Student sex: F = female, M = male",
    "age": "Student age in years",
    "address": "Home address type: U = urban, R = rural",
    "famsize": "Family size: LE3 = 3 or fewer, GT3 = more than 3",
    "Pstatus": "Parents' cohabitation status: T = together, A = apart",
    "Medu": "Mother's education: 0=none, 1=primary(4th), 2=5th-9th, 3=secondary, 4=higher",
    "Fedu": "Father's education: 0=none, 1=primary(4th), 2=5th-9th, 3=secondary, 4=higher",
    "Mjob": "Mother's job: teacher, health, services, at_home, other",
    "Fjob": "Father's job: teacher, health, services, at_home, other",
    "reason": "Reason for choosing this school: home, reputation, course, other",
    "nursery": "Attended nursery school: yes / no",
    "internet": "Internet access at home: yes / no",
    # --- subject-specific (suffixed) ---
    "guardian": "Student's guardian: mother, father, other",
    "traveltime": "Home-to-school travel time: 1=<15min, 2=15-30min, 3=30-60min, 4=>60min",
    "studytime": "Weekly study time: 1=<2h, 2=2-5h, 3=5-10h, 4=>10h",
    "failures": "Number of past class failures (n if 1<=n<3, else 4)",
    "schoolsup": "Extra educational support from school: yes / no",
    "famsup": "Family educational support: yes / no",
    "paid": "Extra paid classes in this subject: yes / no",
    "activities": "Extra-curricular activities: yes / no",
    "higher": "Wants to take higher education: yes / no",
    "romantic": "In a romantic relationship: yes / no",
    "famrel": "Quality of family relationships: 1=very bad to 5=excellent",
    "freetime": "Free time after school: 1=very low to 5=very high",
    "goout": "Going out with friends: 1=very low to 5=very high",
    "Dalc": "Workday alcohol consumption: 1=very low to 5=very high",
    "Walc": "Weekend alcohol consumption: 1=very low to 5=very high",
    "health": "Current health status: 1=very bad to 5=very good",
    "absences": "Number of school absences",
    "G1": "First period grade (0-20)",
    "G2": "Second period grade (0-20)",
    "G3": "FINAL grade (0-20) - the primary target variable",
}

DERIVED = {
    "absences_mat_capped": "absences_mat after IQR winsorisation (added by 01_data_prep.py)",
    "absences_por_capped": "absences_por after IQR winsorisation (added by 01_data_prep.py)",
    "G3_avg": "Mean of G3_mat and G3_por - overall performance (added)",
    "G3_diff": "G3_mat minus G3_por - positive = stronger at Mathematics (added)",
    "band_mat": "Five-level grade band for G3_mat, Erasmus scale (added)",
    "band_por": "Five-level grade band for G3_por, Erasmus scale (added)",
    "pass_mat": "1 if G3_mat >= 10, else 0 (added)",
    "pass_por": "1 if G3_por >= 10, else 0 (added)",
}

KEYS = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu",
        "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet"]


def describe(col):
    if col in DERIVED:
        return DERIVED[col]
    base = col[:-4] if col.endswith(("_mat", "_por")) else col
    text = DESC.get(base, "")
    if col.endswith("_mat"):
        text += "  [Mathematics]"
    elif col.endswith("_por"):
        text += "  [Portuguese]"
    return text


def value_info(s):
    if pd.api.types.is_numeric_dtype(s):
        return f"{s.min():g} to {s.max():g}"
    vals = sorted(str(v) for v in s.dropna().unique())
    return ", ".join(vals) if len(vals) <= 6 else f"{len(vals)} categories"


rows = []
for c in df.columns:
    role = "MERGE KEY" if c in KEYS else ("DERIVED" if c in DERIVED else "attribute")
    rows.append((c, str(df[c].dtype), role, value_info(df[c]), describe(c)))

lines = [
    "# Data Dictionary - `student_clean.csv`",
    "",
    "**DSC4043 Introduction to Data Science | Group Project**",
    "",
    "> Generated automatically from the exported file by `src/_make_data_dictionary.py`.",
    "> Do not edit by hand. If the prep script changes, regenerate this.",
    "",
    "---",
    "",
    "## Read this before you write any code",
    "",
    f"- The file has **{df.shape[0]} rows** (students who took both subjects) "
    f"and **{df.shape[1]} columns**.",
    f"- There are **{int(df.isnull().sum().sum())} missing values**. "
    "The file is already clean - do not clean it again.",
    "- **Columns that exist in both subjects carry a `_mat` or `_por` suffix.** "
    "There is no plain `G3` column. Use `G3_mat` or `G3_por`.",
    "- The 13 **merge keys** have no suffix, because they are identical in both "
    "subjects by definition.",
    "- Ordinal survey scales (1-5) are stored as integers so they can be used in "
    "correlations. Treat them as ordered categories when interpreting.",
    "",
    "### Loading the data",
    "",
    "```python",
    "import pandas as pd",
    "",
    "# Local (running from the repo root)",
    "df = pd.read_csv('data/clean/student_clean.csv')",
    "",
    "# Google Colab - pulls straight from GitHub, no upload needed",
    "URL = 'https://raw.githubusercontent.com/<OWNER>/<REPO>/main/data/clean/student_clean.csv'",
    "df = pd.read_csv(URL)",
    "```",
    "",
    "---",
    "",
    "## Columns",
    "",
    "| # | Column | Type | Role | Values / Range | Description |",
    "|---|--------|------|------|----------------|-------------|",
]
for i, (c, dt, role, vals, desc) in enumerate(rows, 1):
    lines.append(f"| {i} | `{c}` | {dt} | {role} | {vals} | {desc} |")

lines += [
    "",
    "---",
    "",
    "## Quick reference - the columns you will actually use",
    "",
    "| Purpose | Column |",
    "|---------|--------|",
    "| Final Mathematics grade (main target) | `G3_mat` |",
    "| Final Portuguese grade | `G3_por` |",
    "| Earlier period grades | `G1_mat`, `G2_mat`, `G1_por`, `G2_por` |",
    "| Absences | `absences_mat`, `absences_por` (capped versions available) |",
    "| Study time | `studytime_mat`, `studytime_por` |",
    "| Past failures | `failures_mat`, `failures_por` |",
    "| Alcohol consumption | `Dalc_mat`, `Walc_mat`, `Dalc_por`, `Walc_por` |",
    "| Wants higher education | `higher_mat`, `higher_por` |",
    "| Mother's / father's job | `Mjob`, `Fjob` (no suffix - merge keys) |",
    "| Grade band for count plots | `band_mat`, `band_por` |",
    "",
    "---",
    "",
    "## Source",
    "",
    "Cortez, P., & Silva, A. (2008). *Using data mining to predict secondary "
    "school student performance.* In A. Brito & J. Teixeira (Eds.), "
    "Proceedings of 5th FUture BUsiness TEChnology Conference (pp. 5-12). EUROSIS.",
    "",
    "Dataset: UCI Machine Learning Repository - Student Performance  ",
    "https://archive.ics.uci.edu/dataset/320/student+performance",
    "",
]

out = os.path.join(BASE, "docs", "data_dictionary.md")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    f.write("\n".join(lines))

missing_desc = [c for c, _, _, _, d in rows if not d.strip()]
print(f"Wrote {out}")
print(f"{len(rows)} columns documented. Missing descriptions: {missing_desc or 'none'}")
