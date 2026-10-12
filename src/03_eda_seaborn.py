"""
DSC4043 - INTRODUCTION TO DATA SCIENCE
Group Project | Part A - Exploratory Data Analysis (Seaborn)

OWNER    : AMIR
DUE      : Friday 26 September, 9pm
DELIVERS : 3 Seaborn plots + the APA reference list  (~8 of 60 marks + references)

-----------------------------------------------------------------------
HOW TO USE THIS FILE
-----------------------------------------------------------------------
1. The data is ALREADY CLEANED. Just run this file. Do not clean anything.
2. Fill in each block marked  # TODO  .
3. Column names: read docs/data_dictionary.md. There is NO plain `G3` -
   use `G3_mat` (Mathematics) or `G3_por` (Portuguese).
4. Every plot needs 2-3 sentences in its INTERPRETATION string.
5. IMPORTANT - do PLOT 1 (the heatmap) FIRST and tell Basit when it is
   exported. His statistical analysis section references it.
6. Run it:   python src/03_eda_seaborn.py
-----------------------------------------------------------------------
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------------------------------
# SETUP - already done for you, do not change
# --------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(BASE_DIR, "data", "clean", "student_clean.csv"))
print(f"Loaded {df.shape[0]} students x {df.shape[1]} columns\n")

sns.set_theme(style="whitegrid", palette="deep", font_scale=1.0)
plt.rcParams.update({"savefig.dpi": 300, "savefig.bbox": "tight"})


def save(fig, name):
    path = os.path.join(FIG_DIR, name)
    fig.savefig(path)
    plt.close(fig)
    print(f"  saved -> figures/{name}")


# ==========================================================================
# PLOT 5 - Correlation heatmap   *** DO THIS ONE FIRST - BASIT NEEDS IT ***
# ==========================================================================
print("=" * 70)
print("PLOT 5 - Correlation heatmap")
print("=" * 70)

# A focused subset reads far better than all 35 numeric columns at once.
HEATMAP_VARS = [
    "G1_mat", "G2_mat", "G3_mat", "G3_por",
    "failures_mat", "studytime_mat", "absences_mat",
    "goout_mat", "Dalc_mat", "Walc_mat", "health_mat",
    "age", "Medu", "Fedu",
]

fig, ax = plt.subplots(figsize=(10, 8))

corr = df[HEATMAP_VARS].corr()
mask = np.triu(np.ones_like(corr, dtype=bool), k=1)
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt=".2f",
    cmap="RdBu_r",
    center=0,
    vmin=-1,
    vmax=1,
    square=True,
    linewidths=0.5,
    annot_kws={"size": 8},
    cbar_kws={"label": "Pearson correlation coefficient (r)", "shrink": 0.8},
    ax=ax,
)
ax.set_title("Correlation Matrix of Key Numeric Variables", pad=14, weight="bold")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
fig.tight_layout()
corr.round(3).to_csv(os.path.join(BASE_DIR, "docs", "correlation_matrix.csv"))

save(fig, "plot5_heatmap_correlation.png")

PLOT5_INTERPRETATION = """
Previous Mathematics grades had the strongest positive relationships with
the final Mathematics grade: G2_mat correlated at r = 0.903 and G1_mat at
r = 0.805. Past failures had the clearest negative association with final
performance (r = -0.381), whereas study time, absences, going out, alcohol
consumption and health were only weakly related to G3_mat. These values show
association rather than causation, and the strong grade-to-grade correlations
partly reflect that the assessments measure the same students over time.
"""


# ==========================================================================
# PLOT 6 - Boxplot: final grade by desire for higher education
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 6 - G3_mat by higher_mat")
print("=" * 70)

fig, ax = plt.subplots(figsize=(7, 5))

group_stats = (
    df.groupby("higher_mat", observed=True)["G3_mat"]
    .agg(n="size", mean="mean", median="median")
    .reindex(["no", "yes"])
)

sns.boxplot(
    data=df,
    x="higher_mat",
    y="G3_mat",
    order=["no", "yes"],
    hue="higher_mat",
    palette={"no": "#E4715F", "yes": "#2F4B7C"},
    legend=False,
    width=0.55,
    ax=ax,
)
sns.stripplot(
    data=df,
    x="higher_mat",
    y="G3_mat",
    order=["no", "yes"],
    color="black",
    alpha=0.28,
    size=3,
    jitter=0.20,
    ax=ax,
)
ax.axhline(10, linestyle="--", color="grey", linewidth=1.2, label="Pass mark (10)")
ax.set_xlabel("Aspiration to enter higher education")
ax.set_ylabel("Final Mathematics grade (0-20)")
ax.set_xticks(
    [0, 1],
    labels=[
        f"No (n={int(group_stats.loc['no', 'n'])})",
        f"Yes (n={int(group_stats.loc['yes', 'n'])})",
    ],
)
ax.set_title("Final Mathematics Grade by Higher-Education Aspiration", pad=12, weight="bold")
ax.set_ylim(-0.5, 20.8)
ax.legend(loc="upper left", frameon=True)
for xpos, response in enumerate(["no", "yes"]):
    mean = group_stats.loc[response, "mean"]
    ax.scatter(
        xpos,
        mean,
        marker="D",
        s=44,
        facecolor="white",
        edgecolor="black",
        linewidth=1.0,
        zorder=5,
    )
    ax.annotate(
        f"Mean = {mean:.2f}",
        (xpos, mean),
        xytext=(8, 9),
        textcoords="offset points",
        ha="left",
        va="bottom",
        fontsize=9,
        weight="bold",
    )
fig.tight_layout()

save(fig, "plot6_box_higher_education.png")

PLOT6_INTERPRETATION = """
Students who intended to enter higher education achieved a higher mean final
Mathematics grade (M = 10.63, n = 364) than students who did not (M = 5.50,
n = 18). The difference is substantial, but the 'no' group represents only
4.7% of the sample, so its distribution is estimated from very few students.
The plot therefore supports an association between aspiration and performance,
not a claim that higher-education aspirations cause higher grades.
"""


# ==========================================================================
# PLOT 7 - Countplot: grade band distribution across both subjects
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 7 - Grade band distribution, Mathematics vs Portuguese")
print("=" * 70)

fig, ax = plt.subplots(figsize=(9, 5))

bands = pd.concat([
    df[["band_mat"]].rename(columns={"band_mat": "band"}).assign(Subject="Mathematics"),
    df[["band_por"]].rename(columns={"band_por": "band"}).assign(Subject="Portuguese"),
], ignore_index=True)
order = [
    "V (fail)",
    "IV (sufficient)",
    "III (satisfactory)",
    "II (good)",
    "I (excellent/very good)",
]
sns.countplot(
    data=bands,
    x="band",
    hue="Subject",
    order=order,
    palette={"Mathematics": "#2F4B7C", "Portuguese": "#F28E2B"},
    ax=ax,
)
for container in ax.containers:
    ax.bar_label(container, fmt="%d", padding=2, fontsize=9)
ax.set_title("Grade-Band Distribution Across Subjects", pad=12, weight="bold")
ax.set_xlabel("Final-grade band")
ax.set_ylabel("Number of students")
ax.set_ylim(0, 140)
ax.legend(title="Subject", frameon=True)
plt.setp(ax.get_xticklabels(), rotation=18, ha="right")
fig.tight_layout()

save(fig, "plot7_count_grade_bands.png")

PLOT7_INTERPRETATION = """
Mathematics had 127 students (33.2%) in the fail band, compared with 32
(8.4%) in Portuguese. Portuguese results clustered most strongly in the
satisfactory band, whereas the Mathematics distribution was shifted toward
the lower bands. The moderate correlation between the two final grades
(r = 0.480) indicates that performance was related across subjects but not
consistent enough for one subject to be treated as a substitute for the other.
"""


# ==========================================================================
# APA REFERENCE LIST - Amir also owns this
# ==========================================================================
print("\n" + "=" * 70)
print("APA REFERENCES - copy into the report's reference list")
print("=" * 70)

REFERENCES = """
Cortez, P., & Silva, A. (2008). Using data mining to predict secondary
    school student performance. In A. Brito & J. Teixeira (Eds.),
    Proceedings of 5th FUture BUsiness TEChnology Conference (pp. 5-12).
    EUROSIS.

Cortez, P. (2008). Student performance [Data set]. UCI Machine
    Learning Repository. https://doi.org/10.24432/C5TG7T

Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen,
    P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N. J.,
    Kern, R., Picus, M., Hoyer, S., van Kerkwijk, M. H., Brett, M., Haldane,
    A., del Rio, J. F., Wiebe, M., Peterson, P., ... Oliphant, T. E. (2020).
    Array programming with NumPy. Nature, 585(7825), 357-362.
    https://doi.org/10.1038/s41586-020-2649-2

Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in
    Science & Engineering, 9(3), 90-95. https://doi.org/10.1109/MCSE.2007.55

The pandas development team. (2026). pandas-dev/pandas: Pandas [Computer
    software]. Zenodo. https://doi.org/10.5281/zenodo.3509134

Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T.,
    Cournapeau, D., Burovski, E., Peterson, P., Weckesser, W., Bright, J.,
    van der Walt, S. J., Brett, M., Wilson, J., Millman, K. J., Mayorov, N.,
    Nelson, A. R. J., Jones, E., Kern, R., Larson, E., ... Vázquez-Baeza, Y.
    (2020). SciPy 1.0: Fundamental algorithms for scientific computing in
    Python. Nature Methods, 17(3), 261-272.
    https://doi.org/10.1038/s41592-019-0686-2

Waskom, M. L. (2021). seaborn: Statistical data visualization. Journal of
    Open Source Software, 6(60), 3021. https://doi.org/10.21105/joss.03021
"""
print(REFERENCES)


# ==========================================================================
# DONE
# ==========================================================================
print("=" * 70)
print("AMIR'S SECTION COMPLETE")
print("Checklist before you commit:")
print("  [ ] 3 PNG files exist in figures/")
print("  [ ] docs/correlation_matrix.csv exists - TELL BASIT")
print("  [ ] All 3 INTERPRETATION strings are written")
print("  [ ] Reference list checked and the UCI entry added")
print("=" * 70)

for name, text in [("PLOT 5", PLOT5_INTERPRETATION),
                   ("PLOT 6", PLOT6_INTERPRETATION),
                   ("PLOT 7", PLOT7_INTERPRETATION)]:
    flag = "  <-- STILL A TODO" if "TODO" in text else ""
    print(f"{name}:{flag}")
