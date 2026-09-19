"""
DSC4043 - INTRODUCTION TO DATA SCIENCE
Group Project | Part A - Data Preparation & Cleaning

OWNER : Aliff
STATUS: FOUNDATION SCRIPT - do not edit unless you are Aliff.

WHAT THIS DOES
--------------
Loads the two raw UCI Student Performance files, merges them into one
analysis dataset, cleans it, and exports `data/clean/student_clean.csv`.

Every other script in this project reads ONLY that exported file.
Nobody re-cleans the raw data.

Dataset : Student Performance (Cortez & Silva, 2008)
Source  : https://archive.ics.uci.edu/dataset/320/student+performance
Run     : python src/01_data_prep.py
"""

import os
import pandas as pd
import numpy as np

# --------------------------------------------------------------------------
# 0. CONFIG
# --------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
CLEAN_DIR = os.path.join(BASE_DIR, "data", "clean")
os.makedirs(CLEAN_DIR, exist_ok=True)

# The 13 attributes that identify the SAME student across both files.
# Source: the merge procedure documented by Cortez & Silva with the dataset.
# Merging on anything else (e.g. all shared columns) gives the wrong answer.
IDENTITY_KEYS = [
    "school", "sex", "age", "address", "famsize", "Pstatus",
    "Medu", "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet",
]

EXPECTED_MATCHES = 382  # documented ground truth - used as an assertion below


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# --------------------------------------------------------------------------
# 1. LOAD THE RAW DATA
# --------------------------------------------------------------------------
section("1. LOADING RAW DATA")

# NOTE: these files are SEMICOLON-delimited, not comma-delimited.
# Reading them with the default sep=',' gives one giant single column.
mat = pd.read_csv(os.path.join(RAW_DIR, "student-mat.csv"), sep=";")
por = pd.read_csv(os.path.join(RAW_DIR, "student-por.csv"), sep=";")

print(f"student-mat.csv (Mathematics) : {mat.shape[0]} rows x {mat.shape[1]} columns")
print(f"student-por.csv (Portuguese)  : {por.shape[0]} rows x {por.shape[1]} columns")
print(f"\nColumns are identical in both files: {list(mat.columns) == list(por.columns)}")


# --------------------------------------------------------------------------
# 2. INSPECT BEFORE TOUCHING ANYTHING
# --------------------------------------------------------------------------
section("2. PRE-MERGE INSPECTION")

for name, df in [("Mathematics", mat), ("Portuguese", por)]:
    print(f"\n--- {name} ---")
    print(f"Missing values total : {int(df.isnull().sum().sum())}")
    print(f"Duplicate rows       : {int(df.duplicated().sum())}")
    n_num = len(df.select_dtypes(include=np.number).columns)
    print(f"Numeric columns      : {n_num}")
    print(f"Categorical columns  : {df.shape[1] - n_num}")

print("\nNOTE FOR THE REPORT: the raw files contain no null values. The missing")
print("values handled in step 4 arise from the MERGE, which is a genuine and")
print("more realistic source of missingness than pre-injected nulls.")


# --------------------------------------------------------------------------
# 3. THE MERGE (inner) - this is the analysis dataset
# --------------------------------------------------------------------------
section("3. MERGING THE TWO DATASETS (INNER JOIN)")

merged = pd.merge(
    mat, por,
    on=IDENTITY_KEYS,
    how="inner",
    suffixes=("_mat", "_por"),
)

print(f"Merge keys ({len(IDENTITY_KEYS)}): {IDENTITY_KEYS}")
print(f"\nResult: {merged.shape[0]} students x {merged.shape[1]} columns")
print(f"These are students who took BOTH Mathematics and Portuguese.")

assert merged.shape[0] == EXPECTED_MATCHES, (
    f"STOP. Expected {EXPECTED_MATCHES} matched students but got {merged.shape[0]}. "
    "Do not continue - the merge keys are wrong."
)
print(f"\n[OK] Row count matches the documented ground truth ({EXPECTED_MATCHES}).")

suffixed = sorted({c.rsplit("_", 1)[0] for c in merged.columns if c.endswith(("_mat", "_por"))})
print(f"\nSubject-specific columns (now suffixed _mat / _por): {suffixed}")
print("--> Every downstream script MUST use the suffixed names. See docs/data_dictionary.md")

# --- Key uniqueness check (report this as a LIMITATION) -------------------
mat_dup_keys = int(mat.duplicated(subset=IDENTITY_KEYS, keep=False).sum())
por_dup_keys = int(por.duplicated(subset=IDENTITY_KEYS, keep=False).sum())
naive_expected = len(mat) + len(por) - merged.shape[0]

print(f"\nKey uniqueness check:")
print(f"  Mathematics rows sharing all 13 key values : {mat_dup_keys}")
print(f"  Portuguese  rows sharing all 13 key values : {por_dup_keys}")
print("""
  LIMITATION FOR THE REPORT: the 13 attributes do not uniquely identify every
  student. A small number of students share an identical demographic profile,
  so the join is many-to-many rather than strictly one-to-one and a few rows
  represent a probable rather than certain match. 382 is nonetheless the
  figure published with the dataset, so we adopt it for comparability with
  the literature. This is a real constraint on our conclusions and is
  discussed in Section 5 of the report.""")


# --------------------------------------------------------------------------
# 4. THE OUTER MERGE - where our missing values come from
# --------------------------------------------------------------------------
section("4. MISSING VALUE ANALYSIS (OUTER JOIN)")

outer = pd.merge(
    mat, por,
    on=IDENTITY_KEYS,
    how="outer",
    suffixes=("_mat", "_por"),
    indicator=True,
)

counts = outer["_merge"].value_counts()
n_both = int(counts.get("both", 0))
n_mat_only = int(counts.get("left_only", 0))
n_por_only = int(counts.get("right_only", 0))

print(f"Total unique student records : {outer.shape[0]}")
print(f"  In both subjects           : {n_both}")
print(f"  Mathematics only           : {n_mat_only}  -> all _por columns are NaN")
print(f"  Portuguese only            : {n_por_only}  -> all _mat columns are NaN")

missing_pct = (outer.isnull().sum() / len(outer) * 100).round(2)
missing_pct = missing_pct[missing_pct > 0].sort_values(ascending=False)
print(f"\nColumns containing NaN after the outer join: {len(missing_pct)}")
print("Top 10 by percentage missing:")
print(missing_pct.head(10).to_string())

print("""
HANDLING STRATEGY (write this up in the report):
  Listwise deletion - we keep only the 382 complete cases (the inner join).
  Justification: our central research question compares the SAME student's
  performance across two subjects. A record missing one subject entirely
  cannot answer that question, and imputing a whole subject's grades from
  other students would fabricate the very relationship we are measuring.
  The outer join above is retained as an audit trail of what was excluded.
""")

# Demonstrate an imputation technique on the audit frame (not on the analysis
# data) so the report can show we considered and tested the alternative.
audit = outer.copy()
before = audit["G3_por"].isnull().sum()
audit["G3_por_median_imputed"] = audit["G3_por"].fillna(audit["G3_por"].median())
print(f"Imputation demonstration: G3_por had {before} NaN; median imputation "
      f"fills them with {audit['G3_por'].median():.1f}. "
      "Not used in the final analysis - shown for comparison only.")


# --------------------------------------------------------------------------
# 5. CLEANING THE ANALYSIS DATASET
# --------------------------------------------------------------------------
section("5. CLEANING")

df = merged.copy()

# 5.1 Duplicates ------------------------------------------------------------
dupes = int(df.duplicated().sum())
df = df.drop_duplicates()
print(f"5.1 Duplicate rows removed : {dupes}")

# 5.2 Whitespace in categorical columns -------------------------------------
# Version-safe way to find text columns across pandas 2.x and 3.x
cat_cols = [c for c in df.columns if not pd.api.types.is_numeric_dtype(df[c])]
for c in cat_cols:
    df[c] = df[c].str.strip()
print(f"5.2 Whitespace stripped from {len(cat_cols)} categorical columns")

# 5.3 Correct dtypes --------------------------------------------------------
# Ordinal survey scales (1-5) are stored as int64 but are ordered categories.
# We keep them numeric for correlation, but flag them in the data dictionary.
ordinal_cols = [c for c in df.columns if c.split("_")[0] in
                ("Medu", "Fedu", "traveltime", "studytime", "famrel",
                 "freetime", "goout", "Dalc", "Walc", "health")]
for c in cat_cols:
    df[c] = df[c].astype("category")
print(f"5.3 Converted {len(cat_cols)} object columns to 'category' dtype")
print(f"    Ordinal 1-5 scales kept numeric for correlation: {len(ordinal_cols)} columns")

# 5.4 Outlier treatment on absences (IQR method) ----------------------------
print("\n5.4 Outlier treatment - IQR method on absences")
for col in ["absences_mat", "absences_por"]:
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    n_out = int(((df[col] < lo) | (df[col] > hi)).sum())
    df[col + "_capped"] = df[col].clip(lower=lo, upper=hi)
    print(f"    {col:16s} Q1={q1:5.1f} Q3={q3:5.1f} IQR={iqr:5.1f} "
          f"bounds=[{lo:.1f}, {hi:.1f}] outliers={n_out}")
print("    Strategy: WINSORISED (capped), not deleted. High absenteeism is")
print("    genuine signal, not measurement error - deleting it would bias the")
print("    absences-vs-grade relationship. Original columns are kept alongside.")

# 5.5 Range validation ------------------------------------------------------
print("\n5.5 Range validation")
grade_cols = [c for c in df.columns if c.startswith(("G1", "G2", "G3"))]
bad = {c: int(((df[c] < 0) | (df[c] > 20)).sum()) for c in grade_cols}
print(f"    Grades outside the valid 0-20 scale: {sum(bad.values())} "
      f"across {len(grade_cols)} grade columns")
print(f"    Ages outside 15-22: {int(((df['age'] < 15) | (df['age'] > 22)).sum())}")


# --------------------------------------------------------------------------
# 6. FEATURE ENGINEERING
# --------------------------------------------------------------------------
section("6. DERIVED COLUMNS")

# Mean grade across both subjects - a single overall performance measure
df["G3_avg"] = ((df["G3_mat"] + df["G3_por"]) / 2).round(2)

# Difference between subjects - positive means stronger at Maths
df["G3_diff"] = df["G3_mat"] - df["G3_por"]

# Five-level grade band (Cortez & Silva 2008, Table 2 - Erasmus scale)
def grade_band(g):
    if g >= 16:
        return "I (excellent/very good)"
    if g >= 14:
        return "II (good)"
    if g >= 12:
        return "III (satisfactory)"
    if g >= 10:
        return "IV (sufficient)"
    return "V (fail)"

df["band_mat"] = df["G3_mat"].apply(grade_band).astype("category")
df["band_por"] = df["G3_por"].apply(grade_band).astype("category")

# Binary pass/fail on the 0-20 Portuguese scale (pass = 10)
df["pass_mat"] = (df["G3_mat"] >= 10).astype(int)
df["pass_por"] = (df["G3_por"] >= 10).astype(int)

print("Added: G3_avg, G3_diff, band_mat, band_por, pass_mat, pass_por")
print(f"\nGrade band distribution (Mathematics):")
print(df["band_mat"].value_counts().sort_index().to_string())
print(f"\nPass rate - Mathematics: {df['pass_mat'].mean():.1%} | "
      f"Portuguese: {df['pass_por'].mean():.1%}")


# --------------------------------------------------------------------------
# 7. EXPORT
# --------------------------------------------------------------------------
section("7. EXPORT")

out_path = os.path.join(CLEAN_DIR, "student_clean.csv")
df.to_csv(out_path, index=False)

audit_path = os.path.join(CLEAN_DIR, "merge_audit_outer.csv")
outer.drop(columns=["_merge"]).to_csv(audit_path, index=False)

print(f"Analysis dataset -> {out_path}")
print(f"  {df.shape[0]} rows x {df.shape[1]} columns, "
      f"{int(df.isnull().sum().sum())} missing values")
print(f"Merge audit      -> {audit_path}")
print(f"  {outer.shape[0]} rows (all students from both files)")

print("\n" + "=" * 70)
print("DATA PREPARATION COMPLETE")
print("Yasierul, Amir and Ramzi: load data/clean/student_clean.csv only.")
print("Column names are documented in docs/data_dictionary.md")
print("=" * 70)
