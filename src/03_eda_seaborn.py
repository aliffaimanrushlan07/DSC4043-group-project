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
5. IMPORTANT - do PLOT 1 (the heatmap) FIRST and tell Ramzi when it is
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
# PLOT 5 - Correlation heatmap   *** DO THIS ONE FIRST - RAMZI NEEDS IT ***
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

# TODO 1: build the heatmap.
#   corr = df[HEATMAP_VARS].corr()
#   mask = np.triu(np.ones_like(corr, dtype=bool))   # hide the mirror half
#   sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',
#               center=0, vmin=-1, vmax=1, square=True,
#               linewidths=0.5, cbar_kws={'label': 'Pearson r'}, ax=ax)
#   ax.set_title('Correlation matrix of key numeric variables')
#   Then export the numbers for Ramzi:
#   corr.round(3).to_csv(os.path.join(BASE_DIR, 'docs', 'correlation_matrix.csv'))

save(fig, "plot5_heatmap_correlation.png")

PLOT5_INTERPRETATION = """
TODO: 2-3 sentences. The strongest relationship by far is G2_mat with
G3_mat at about +0.90 - the second period grade almost determines the
final one. Past failures show the strongest negative relationship at
about -0.38. Point out how weak most of the social variables are
(going out, alcohol, health all sit near zero), which is itself a
finding worth stating.
"""


# ==========================================================================
# PLOT 6 - Boxplot: final grade by desire for higher education
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 6 - G3_mat by higher_mat")
print("=" * 70)

fig, ax = plt.subplots(figsize=(7, 5))

# TODO 2: boxplot.
#   sns.boxplot(data=df, x='higher_mat', y='G3_mat', hue='higher_mat',
#               palette=['#E4715F', '#2F4B7C'], legend=False, ax=ax)
#   Overlay the individual students so the group sizes are visible:
#   sns.stripplot(data=df, x='higher_mat', y='G3_mat', color='black',
#                 alpha=0.25, size=3, ax=ax)
#   ax.axhline(10, linestyle='--', color='grey', label='Pass mark')
#   ax.set_xlabel('Wants to take higher education')
#   ax.set_ylabel('Final Mathematics grade (0-20)')

save(fig, "plot6_box_higher_education.png")

PLOT6_INTERPRETATION = """
TODO: 2-3 sentences. This is the single largest gap in the whole dataset:
students who want higher education average about 10.6 versus about 5.5 for
those who do not - roughly double. BUT only 18 of the 382 students said no,
so the boxplot for that group rests on very few observations. State both
the size of the effect AND that caveat; the rubric rewards that kind of
careful reading.
"""


# ==========================================================================
# PLOT 7 - Countplot: grade band distribution across both subjects
# ==========================================================================
print("\n" + "=" * 70)
print("PLOT 7 - Grade band distribution, Mathematics vs Portuguese")
print("=" * 70)

fig, ax = plt.subplots(figsize=(9, 5))

# TODO 3: reshape to long form, then draw a grouped countplot.
#   bands = pd.concat([
#       df[['band_mat']].rename(columns={'band_mat': 'band'}).assign(Subject='Mathematics'),
#       df[['band_por']].rename(columns={'band_por': 'band'}).assign(Subject='Portuguese'),
#   ])
#   order = ['V (fail)', 'IV (sufficient)', 'III (satisfactory)',
#            'II (good)', 'I (excellent/very good)']
#   sns.countplot(data=bands, x='band', hue='Subject', order=order, ax=ax)
#   plt.setp(ax.get_xticklabels(), rotation=20, ha='right')

save(fig, "plot7_count_grade_bands.png")

PLOT7_INTERPRETATION = """
TODO: 2-3 sentences. Mathematics has 127 students in the fail band against
only 32 in Portuguese - the same students perform very differently in the
two subjects. Describe the shape: Portuguese clusters in the middle bands
while Mathematics is spread toward the bottom. Link this to the moderate
+0.48 correlation between the two final grades: related, but far from
interchangeable.
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

Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen,
    P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N. J.,
    Kern, R., Picus, M., Hoyer, S., van Kerkwijk, M. H., Brett, M., Haldane,
    A., del Rio, J. F., Wiebe, M., Peterson, P., ... Oliphant, T. E. (2020).
    Array programming with NumPy. Nature, 585(7825), 357-362.
    https://doi.org/10.1038/s41586-020-2649-2

Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in
    Science & Engineering, 9(3), 90-95. https://doi.org/10.1109/MCSE.2007.55

The pandas development team. (2024). pandas-dev/pandas: Pandas (Version 2.x)
    [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.3509134

Waskom, M. L. (2021). seaborn: Statistical data visualization. Journal of
    Open Source Software, 6(60), 3021. https://doi.org/10.21105/joss.03021

TODO (Amir): add the UCI repository entry in APA form. Format it as:
    Cortez, P., & Silva, A. (2008). Student performance [Data set].
    UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T
Check the DOI on the UCI page before you submit it.
"""
print(REFERENCES)


# ==========================================================================
# DONE
# ==========================================================================
print("=" * 70)
print("AMIR'S SECTION COMPLETE")
print("Checklist before you commit:")
print("  [ ] 3 PNG files exist in figures/")
print("  [ ] docs/correlation_matrix.csv exists - TELL RAMZI")
print("  [ ] All 3 INTERPRETATION strings are written")
print("  [ ] Reference list checked and the UCI entry added")
print("=" * 70)

for name, text in [("PLOT 5", PLOT5_INTERPRETATION),
                   ("PLOT 6", PLOT6_INTERPRETATION),
                   ("PLOT 7", PLOT7_INTERPRETATION)]:
    flag = "  <-- STILL A TODO" if "TODO" in text else ""
    print(f"{name}:{flag}")
