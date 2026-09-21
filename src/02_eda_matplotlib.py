"""
DSC4043 - INTRODUCTION TO DATA SCIENCE
Group Project | Part A - Exploratory Data Analysis (Matplotlib)

OWNER    : YASIERUL
DUE      : Friday 26 September, 9pm
DELIVERS : Summary measures table + 4 Matplotlib plots  (~12 of 60 marks)

-----------------------------------------------------------------------
HOW TO USE THIS FILE
-----------------------------------------------------------------------
1. The data is ALREADY CLEANED. Just run this file - it loads
   data/clean/student_clean.csv for you. Do not clean anything.
2. Fill in each block marked  # TODO  . The skeleton, the figure saving
   and the file paths are already done.
3. Column names: read docs/data_dictionary.md. Remember there is NO plain
   `G3` column - it is `G3_mat` (Mathematics) or `G3_por` (Portuguese).
4. Every plot needs 2-3 sentences of interpretation written into the
   INTERPRETATION string below it. The rubric awards marks for
   explanation, not just for the picture. Plots with no interpretation
   cap the whole group at 10/20 for this section.
5. Run it:   python src/02_eda_matplotlib.py
   Check that 4 PNG files appear in figures/ and that nothing errors.
-----------------------------------------------------------------------
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")            # lets the script run without a display
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# SETUP - already done for you, do not change
# --------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(BASE_DIR, "data", "clean", "student_clean.csv"))
print(f"Loaded {df.shape[0]} students x {df.shape[1]} columns\n")

plt.rcParams.update({
    "figure.figsize": (8, 5),
    "figure.dpi": 110,
    "savefig.dpi": 300,           # 300 dpi so figures stay sharp in the report
    "savefig.bbox": "tight",
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

NAVY = "#2F4B7C"
TEAL = "#3C8DAD"
CORAL = "#E4715F"


def save(fig, name):
    path = os.path.join(FIG_DIR, name)
    fig.savefig(path)
    plt.close(fig)
    print(f"  saved -> figures/{name}")


# ==========================================================================
# PART 1 - SUMMARY MEASURES TABLE
# ==========================================================================
print("=" * 70)
print("PART 1 - SUMMARY MEASURES")
print("=" * 70)

KEY_VARS = ["G1_mat", "G2_mat", "G3_mat", "G3_por", "G3_avg",
            "absences_mat", "absences_por", "age", "failures_mat"]

# TODO 1: produce the summary table.
#   Hint: summary = df[KEY_VARS].describe().T.round(2)
#   Then add a median column and save it to docs/ as a CSV so it can be
#   pasted into the report:
#       summary.to_csv(os.path.join(BASE_DIR, 'docs', 'summary_measures.csv'))
summary = None  # <-- replace

if summary is not None:
    print(summary.to_string())

SUMMARY_INTERPRETATION = """
TODO: 2-3 sentences. Point out that the mean final Maths grade is around
10.4 out of 20 with a standard deviation of about 4.7, which is a wide
spread for a 0-20 scale. Note the minimum of 0 - students who scored
nothing - and what that does to the distribution.
"""


# ==========================================================================
# PART 2 - PLOT 1 : Histogram, distribution of final Mathematics grade
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 1 - Histogram of G3_mat")
print("=" * 70)

fig, ax = plt.subplots()

# TODO 2: draw the histogram.
#   ax.hist(df['G3_mat'], bins=21, range=(0, 21), color=NAVY, edgecolor='white')
#   Add a dashed vertical line at the pass mark:
#   ax.axvline(10, color=CORAL, linestyle='--', linewidth=2, label='Pass mark (10)')
#   ax.set_xlabel(...), ax.set_ylabel(...), ax.set_title(...), ax.legend()

save(fig, "plot1_hist_g3_mat.png")

PLOT1_INTERPRETATION = """
TODO: 2-3 sentences. The distribution is roughly bell-shaped but has a
noticeable spike at zero. Explain what a zero final grade represents
(students who dropped out or did not sit the exam) and why that matters
for the mean. About 67% of students are at or above the pass mark of 10.
"""


# ==========================================================================
# PART 3 - PLOT 2 : Bar chart, mean grade by weekly study time
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 2 - Mean G3_mat by studytime_mat")
print("=" * 70)

# TODO 3: compute the group means.
#   means = df.groupby('studytime_mat')['G3_mat'].mean()
#   counts = df.groupby('studytime_mat')['G3_mat'].count()
#   Labels for the x axis: ['<2 hrs', '2-5 hrs', '5-10 hrs', '>10 hrs']
#   Draw with ax.bar(...) and annotate each bar with its n using ax.text(...)

fig, ax = plt.subplots()
# ... your code here
save(fig, "plot2_bar_studytime.png")

PLOT2_INTERPRETATION = """
TODO: 2-3 sentences. The relationship is positive but surprisingly weak -
students studying more than 5 hours average about 11.3 versus about 10.1
for those studying under 5. Mention that the two highest study-time groups
are small (62 and 27 students), so the difference is not as reliable as it
looks. This is a good point to revisit in the Discussion section.
"""


# ==========================================================================
# PART 4 - PLOT 3 : Scatter, absences against final grade
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 3 - absences_mat vs G3_mat")
print("=" * 70)

fig, ax = plt.subplots()

# TODO 4: scatter plot.
#   ax.scatter(df['absences_mat'], df['G3_mat'], alpha=0.5, color=TEAL,
#              edgecolors='white', linewidth=0.5)
#   Add a trend line:
#   m, b = np.polyfit(df['absences_mat'], df['G3_mat'], 1)
#   xs = np.linspace(df['absences_mat'].min(), df['absences_mat'].max(), 100)
#   ax.plot(xs, m*xs + b, color=CORAL, linewidth=2, label=f'Trend (slope={m:.3f})')

save(fig, "plot3_scatter_absences.png")

PLOT3_INTERPRETATION = """
TODO: 2-3 sentences. The correlation is almost exactly zero (about +0.03),
which is genuinely counter-intuitive - absences barely predict the final
grade here. Explain the likely reason: the students with the very highest
absences are a small group, and some of them still perform well. Say
plainly that the expected negative relationship does NOT appear in this
dataset. Reporting an unexpected result honestly scores better than
pretending the trend exists.
"""


# ==========================================================================
# PART 5 - PLOT 4 : Grouped bar, grade progression G1 -> G2 -> G3
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 4 - Grade progression across the three periods")
print("=" * 70)

fig, ax = plt.subplots()

# TODO 5: grouped bar chart comparing the two subjects across three periods.
#   periods = ['G1', 'G2', 'G3']
#   maths = [df['G1_mat'].mean(), df['G2_mat'].mean(), df['G3_mat'].mean()]
#   port  = [df['G1_por'].mean(), df['G2_por'].mean(), df['G3_por'].mean()]
#   x = np.arange(3); width = 0.35
#   ax.bar(x - width/2, maths, width, label='Mathematics', color=NAVY)
#   ax.bar(x + width/2, port,  width, label='Portuguese',  color=TEAL)
#   ax.set_xticks(x); ax.set_xticklabels(['Period 1', 'Period 2', 'Final'])

save(fig, "plot4_grade_progression.png")

PLOT4_INTERPRETATION = """
TODO: 2-3 sentences. Portuguese grades sit consistently above Mathematics
across all three periods. Note whether the gap widens or stays constant,
and that both subjects dip slightly or hold steady from period 2 to the
final grade. Link this to the very high G2-to-G3 correlation that Basit
reports in the statistical analysis.
"""


# ==========================================================================
# DONE
# ==========================================================================
print("\n" + "=" * 70)
print("YASIERUL'S SECTION COMPLETE")
print("Checklist before you commit:")
print("  [ ] 4 PNG files exist in figures/")
print("  [ ] docs/summary_measures.csv exists")
print("  [ ] All 5 INTERPRETATION strings are written (no 'TODO' left)")
print("  [ ] Script runs top to bottom with no errors")
print("=" * 70)

for name, text in [("SUMMARY", SUMMARY_INTERPRETATION),
                   ("PLOT 1", PLOT1_INTERPRETATION),
                   ("PLOT 2", PLOT2_INTERPRETATION),
                   ("PLOT 3", PLOT3_INTERPRETATION),
                   ("PLOT 4", PLOT4_INTERPRETATION)]:
    flag = "  <-- STILL A TODO" if "TODO" in text else ""
    print(f"{name}:{flag}")
