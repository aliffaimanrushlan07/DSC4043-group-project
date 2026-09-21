"""
DSC4043 - INTRODUCTION TO DATA SCIENCE
Group Project | Part A - Statistical Analysis

OWNER    : BASIT
DUE      : Friday 26 September, 9pm
DELIVERS : Central tendency, dispersion, correlation + case study  (15 of 60 marks)

-----------------------------------------------------------------------
HOW TO USE THIS FILE
-----------------------------------------------------------------------
1. The data is ALREADY CLEANED. Just run this file. Do not clean anything.
2. Fill in each block marked  # TODO  .
3. Column names: read docs/data_dictionary.md. There is NO plain `G3` -
   use `G3_mat` (Mathematics) or `G3_por` (Portuguese).
4. Your section carries the most marks of the three analysis scripts, and
   the CASE STUDY at the bottom is the piece the rubric singles out. Spend
   most of your time there - roughly one page of written interpretation.
5. Run it:   python src/04_statistical_analysis.py
-----------------------------------------------------------------------
"""

import os
import pandas as pd
import numpy as np
from scipy import stats

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(BASE_DIR, "data", "clean", "student_clean.csv"))
print(f"Loaded {df.shape[0]} students x {df.shape[1]} columns\n")

FOCUS = ["G3_mat", "G3_por", "G3_avg", "absences_mat", "age", "failures_mat"]


def section(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


# ==========================================================================
# 1. MEASURES OF CENTRAL TENDENCY
# ==========================================================================
section("1. CENTRAL TENDENCY")

# TODO 1: build a table of mean, median and mode for every column in FOCUS.
#   Hint:
#   rows = []
#   for col in FOCUS:
#       rows.append({
#           'Variable': col,
#           'Mean':   df[col].mean(),
#           'Median': df[col].median(),
#           'Mode':   df[col].mode().iloc[0],
#       })
#   central = pd.DataFrame(rows).round(2)
central = None  # <-- replace

if central is not None:
    print(central.to_string(index=False))

CENTRAL_INTERPRETATION = """
TODO: 2-3 sentences. For G3_mat the mean is about 10.39 and the median is
11.0 - the mean sits BELOW the median, which tells you the distribution is
pulled left by the cluster of zero grades. Explain what that means for
which measure better represents a typical student, and say why the median
is the safer summary here.
"""


# ==========================================================================
# 2. MEASURES OF DISPERSION
# ==========================================================================
section("2. DISPERSION")

# TODO 2: for each column in FOCUS compute range, variance, standard
# deviation, IQR and the coefficient of variation.
#   Hint:
#   for col in FOCUS:
#       s = df[col]
#       q1, q3 = s.quantile([0.25, 0.75])
#       rows.append({
#           'Variable': col,
#           'Range': s.max() - s.min(),
#           'Variance': s.var(),
#           'Std Dev': s.std(),
#           'IQR': q3 - q1,
#           'CV (%)': s.std() / s.mean() * 100,
#       })
dispersion = None  # <-- replace

if dispersion is not None:
    print(dispersion.to_string(index=False))

DISPERSION_INTERPRETATION = """
TODO: 2-3 sentences. G3_mat has a standard deviation of about 4.69 on a
0-20 scale, so typical students sit roughly 4.7 marks either side of the
average - a wide spread. Compare the coefficient of variation for grades
against absences: absences are far more variable in relative terms.
Explain why CV is the right tool for comparing spread across variables
measured on different scales.
"""


# ==========================================================================
# 3. CORRELATION ANALYSIS
# ==========================================================================
section("3. CORRELATION ANALYSIS")

# TODO 3: compute the full Pearson correlation matrix for the numeric
# columns, then pull out the pairs that matter.
#   numeric = df.select_dtypes(include=np.number)
#   corr = numeric.corr()
#   corr.round(3).to_csv(os.path.join(DOCS_DIR, 'correlation_full.csv'))

PAIRS = [
    ("G2_mat", "G3_mat"),
    ("G1_mat", "G3_mat"),
    ("failures_mat", "G3_mat"),
    ("G3_mat", "G3_por"),
    ("studytime_mat", "G3_mat"),
    ("absences_mat", "G3_mat"),
    ("goout_mat", "G3_mat"),
    ("Medu", "G3_mat"),
    ("age", "G3_mat"),
]

# TODO 4: for each pair report r, the p-value and a strength label.
#   Hint - scipy gives you both at once:
#   r, p = stats.pearsonr(df[a], df[b])
#   Label the strength: |r| >= 0.7 strong, >= 0.4 moderate,
#   >= 0.2 weak, otherwise negligible.
#   Mark significance with p < 0.05.

CORRELATION_INTERPRETATION = """
TODO: 3-4 sentences summarising the pattern. The prior-grade variables
dominate everything else. Past failures are the strongest non-grade
predictor. The social and lifestyle variables are all negligible. State
clearly that correlation does not establish causation - the rubric looks
for this.
"""


# ==========================================================================
# 4. CASE STUDY - THE MAIN DELIVERABLE
# ==========================================================================
section("4. CORRELATION CASE STUDY")

print("""
Pick ONE of these three and write it up properly (about one page).
Option B is the most interesting and the least likely to overlap with
another group's report.

  OPTION A - G2_mat vs G3_mat  (r = +0.903, very strong)
    The second-period grade almost fully determines the final grade.
    Angle: early warning. A student struggling at period 2 is very
    unlikely to recover by the final. Argue for early intervention.
    Risk: it is somewhat obvious, and the two variables are not really
    independent measures.

  OPTION B - G3_mat vs G3_por  (r = +0.480, moderate)   <-- RECOMMENDED
    The SAME 382 students, two different subjects. Moderate correlation
    means general academic ability explains under a quarter of the
    variance (r-squared is about 0.23). Angle: subject-specific ability
    is real and large. 127 students fail Maths while only 32 fail
    Portuguese. Ask what that says about how Mathematics is taught or
    assessed. This is genuinely arguable and shows critical thinking.

    The strongest single fact for this write-up is the ASYMMETRY:
      104 students pass Portuguese but fail Mathematics
        9 students pass Mathematics but fail Portuguese
    A ratio of more than 11 to 1. If the two subjects simply measured
    general ability, those two numbers would be similar. They are not.
    Build your argument around that. (Verify it yourself with the
    crosstab below - do not just quote these numbers.)

  OPTION C - failures_mat vs G3_mat  (r = -0.381, moderate negative)
    Past failure predicts future failure. Angle: the compounding effect
    of falling behind. Discuss the direction-of-causation problem
    explicitly - does failing cause low grades, or does an unmeasured
    third factor cause both?
""")

# TODO 5: run the full analysis for your chosen pair.
#   - r and p value
#   - r-squared, and state the percentage of variance explained
#   - a simple linear fit: slope, intercept  (stats.linregress)
#   - group comparison: for Option B, cross-tabulate pass_mat against
#     pass_por to show how many students pass one subject but not the other
#     Hint: pd.crosstab(df['pass_mat'], df['pass_por'])

CASE_STUDY = """
TODO (Basit): about one page. Structure it like this -

  1. What relationship you tested and why it matters
  2. The numbers: r, p, r-squared, what the regression slope means in
     plain language ("each additional mark in Portuguese is associated
     with X additional marks in Mathematics")
  3. What the result actually means for students and teachers
  4. The limits: correlation is not causation, the sample is 382
     students from two Portuguese schools in one year, and the merge
     keys do not uniquely identify every student (see Aliff's
     Section 2 - reuse his wording)
  5. One sentence on what you would test next with more data
"""


# ==========================================================================
# DONE
# ==========================================================================
section("BASIT'S SECTION COMPLETE")
print("Checklist before you commit:")
print("  [ ] Central tendency table prints")
print("  [ ] Dispersion table prints")
print("  [ ] All 9 correlation pairs reported with r and p")
print("  [ ] docs/correlation_full.csv exists")
print("  [ ] CASE_STUDY is written out in full - this is the big one")
print("  [ ] Script runs top to bottom with no errors")

for name, text in [("CENTRAL TENDENCY", CENTRAL_INTERPRETATION),
                   ("DISPERSION", DISPERSION_INTERPRETATION),
                   ("CORRELATION", CORRELATION_INTERPRETATION),
                   ("CASE STUDY", CASE_STUDY)]:
    flag = "  <-- STILL A TODO" if "TODO" in text else ""
    print(f"{name}:{flag}")
