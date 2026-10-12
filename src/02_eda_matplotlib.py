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

summary = df[KEY_VARS].describe().T
summary.insert(2, "median", df[KEY_VARS].median())
summary.insert(3, "mode", df[KEY_VARS].mode().iloc[0])
summary = summary.rename(columns={"25%": "Q1", "50%": "Q2", "75%": "Q3"})
summary = summary.drop(columns="Q2")          # same as the median column
summary["count"] = summary["count"].astype(int)
summary = summary.round(2)
summary.to_csv(os.path.join(BASE_DIR, "docs", "summary_measures.csv"))
print(summary.to_string())
print("  saved -> docs/summary_measures.csv")

SUMMARY_INTERPRETATION = """
The mean final Mathematics grade is 10.39 out of 20, only just above the
pass mark of 10, and its standard deviation of 4.69 is much larger than
that of Portuguese (2.95), so Mathematics results are far more spread
out. The minimum of 0 pulls the Mathematics mean below its median of 11,
which is why the distribution is skewed to the left. Absences show the
opposite pattern: the mean (5.32) is well above the median (3), and the
maximum of 75 shows that a few students miss a very large number of
classes while most miss very few.
"""


# ==========================================================================
# PART 2 - PLOT 1 : Histogram, distribution of final Mathematics grade
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 1 - Histogram of G3_mat")
print("=" * 70)

fig, ax = plt.subplots()

pass_rate = (df["G3_mat"] >= 10).mean() * 100
n_zero = (df["G3_mat"] == 0).sum()

ax.hist(df["G3_mat"], bins=21, range=(0, 21), color=NAVY, edgecolor="white",
        align="left")
ax.axvline(10, color=CORAL, linestyle="--", linewidth=2,
           label=f"Pass mark (10) - {pass_rate:.1f}% pass")
ax.axvline(df["G3_mat"].mean(), color=TEAL, linestyle=":", linewidth=2,
           label=f"Mean ({df['G3_mat'].mean():.2f})")
ax.annotate(f"{n_zero} students\nscored 0", xy=(0, n_zero), xytext=(2, n_zero + 8),
            arrowprops=dict(arrowstyle="->", color="black"), fontsize=10)
ax.set_xticks(range(0, 21, 2))
ax.set_xlabel("Final Mathematics grade (G3_mat, 0-20)")
ax.set_ylabel("Number of students")
ax.set_title("Distribution of final Mathematics grades (n = 382)")
ax.legend()

save(fig, "plot1_hist_g3_mat.png")
print(f"  pass rate = {pass_rate:.1f}%, zero grades = {n_zero}")

PLOT1_INTERPRETATION = """
Most final Mathematics grades fall between 8 and 15, and 66.8% of students
(255 of 382) reached the pass mark of 10. There is a separate spike of 39
students at exactly 0. Of these, 26 had a non-zero grade in the second
period, so a zero most likely means the student dropped out or did not
sit the final exam rather than a real score of nothing. These zeros pull
the mean (10.39) below the median (11), so the mean understates how a
typical student performed.
"""


# ==========================================================================
# PART 3 - PLOT 2 : Bar chart, mean grade by weekly study time
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 2 - Mean G3_mat by studytime_mat")
print("=" * 70)

means = df.groupby("studytime_mat")["G3_mat"].mean()
counts = df.groupby("studytime_mat")["G3_mat"].count()
labels = ["<2 hrs", "2-5 hrs", "5-10 hrs", ">10 hrs"]
print(pd.DataFrame({"mean_G3_mat": means.round(2), "n": counts}).to_string())

fig, ax = plt.subplots()
bars = ax.bar(labels, means.values, color=[TEAL, TEAL, NAVY, NAVY], width=0.6)
for bar, m, n in zip(bars, means.values, counts.values):
    ax.text(bar.get_x() + bar.get_width() / 2, m + 0.2,
            f"{m:.2f}\n(n = {n})", ha="center", va="bottom", fontsize=10)
ax.axhline(10, color=CORAL, linestyle="--", linewidth=1.5, label="Pass mark (10)")
ax.set_ylim(0, 14)
ax.set_xlabel("Weekly study time (Mathematics)")
ax.set_ylabel("Mean final Mathematics grade")
ax.set_title("Mean final Mathematics grade by weekly study time")
ax.legend(loc="lower right")
save(fig, "plot2_bar_studytime.png")

PLOT2_INTERPRETATION = """
Students who study 5-10 hours or more than 10 hours a week average 11.37
and 11.26, compared with 10.10 for both groups who study less than
5 hours, so more study time is linked with higher grades. The difference
is only about 1.2 marks out of 20, which is smaller than might be
expected, and the two highest groups are small (62 and 27 students), so
their means are less reliable. Study time is also self-reported, so it
may not be accurate.
"""


# ==========================================================================
# PART 4 - PLOT 3 : Scatter, absences against final grade
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 3 - absences_mat vs G3_mat")
print("=" * 70)

fig, ax = plt.subplots()

zero = df["G3_mat"] == 0
r_all = df["absences_mat"].corr(df["G3_mat"])
r_nz = df.loc[~zero, "absences_mat"].corr(df.loc[~zero, "G3_mat"])
print(f"  r (all 382)          = {r_all:.3f}")
print(f"  r (excluding G3 = 0) = {r_nz:.3f}")

ax.scatter(df.loc[~zero, "absences_mat"], df.loc[~zero, "G3_mat"], alpha=0.5,
           color=TEAL, edgecolors="white", linewidth=0.5, label="Students")
ax.scatter(df.loc[zero, "absences_mat"], df.loc[zero, "G3_mat"], alpha=0.8,
           color=CORAL, marker="x", label=f"Final grade = 0 (n = {zero.sum()})")

xs = np.linspace(df["absences_mat"].min(), df["absences_mat"].max(), 100)
m, b = np.polyfit(df["absences_mat"], df["G3_mat"], 1)
ax.plot(xs, m * xs + b, color=NAVY, linewidth=2,
        label=f"Trend, all students (r = {r_all:.2f})")
m2, b2 = np.polyfit(df.loc[~zero, "absences_mat"], df.loc[~zero, "G3_mat"], 1)
ax.plot(xs, m2 * xs + b2, color=NAVY, linewidth=2, linestyle="--",
        label=f"Trend, excluding zeros (r = {r_nz:.2f})")

ax.set_xlabel("Number of absences (Mathematics)")
ax.set_ylabel("Final Mathematics grade (G3_mat)")
ax.set_title("Absences and final Mathematics grade (n = 382)")
ax.legend(fontsize=9)

save(fig, "plot3_scatter_absences.png")

PLOT3_INTERPRETATION = """
Across all 382 students the correlation between absences and the final
Mathematics grade is almost zero (r = 0.03), so the expected negative
relationship does not appear. The reason is the 39 students with a final
grade of 0: every one of them has zero recorded absences, which fits the
idea that they left school or missed the final exam rather than skipping
classes during the year. When those students are excluded, the
correlation becomes weakly negative (r = -0.23), meaning more absences
are linked with slightly lower grades, as expected. Even so, attendance
explains only a small part of the variation in grades.
"""


# ==========================================================================
# PART 5 - PLOT 4 : Grouped bar, grade progression G1 -> G2 -> G3
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 4 - Grade progression across the three periods")
print("=" * 70)

fig, ax = plt.subplots()

maths = [df["G1_mat"].mean(), df["G2_mat"].mean(), df["G3_mat"].mean()]
port = [df["G1_por"].mean(), df["G2_por"].mean(), df["G3_por"].mean()]
x = np.arange(3)
width = 0.35
b1 = ax.bar(x - width / 2, maths, width, label="Mathematics", color=NAVY)
b2 = ax.bar(x + width / 2, port, width, label="Portuguese", color=TEAL)
for bars in (b1, b2):
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
                f"{bar.get_height():.2f}", ha="center", va="bottom", fontsize=10)
ax.axhline(10, color=CORAL, linestyle="--", linewidth=1.5, label="Pass mark (10)")
ax.set_xticks(x)
ax.set_xticklabels(["Period 1 (G1)", "Period 2 (G2)", "Final (G3)"])
ax.set_ylim(0, 16)
ax.set_ylabel("Mean grade (0-20)")
ax.set_title("Grade progression across the three assessment periods")
ax.legend(loc="upper center", ncol=3, fontsize=10)
for label, mv, pv in zip(["G1", "G2", "G3"], maths, port):
    print(f"  {label}: Maths {mv:.2f}  Portuguese {pv:.2f}  gap {pv - mv:.2f}")

save(fig, "plot4_grade_progression.png")

PLOT4_INTERPRETATION = """
Portuguese grades are higher than Mathematics grades in all three periods,
and the two subjects move in opposite directions: the Mathematics mean
falls from 10.86 to 10.71 to 10.39, while the Portuguese mean rises from
12.11 to 12.24 to 12.52. As a result the gap widens from 1.25 marks in
period 1 to 2.13 marks in the final grade. Part of the Mathematics drop
comes from the zero final grades, which rise from none in period 1 to 13
in period 2 and 39 in the final period. Because the second-period grade
is so close to the final grade (r = 0.90 for Mathematics), period 2 would
be a good point to identify students who need help.
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
