# Data Dictionary - `student_clean.csv`

**DSC4043 Introduction to Data Science | Group Project**

> Generated automatically from the exported file by `src/_make_data_dictionary.py`.
> Do not edit by hand. If the prep script changes, regenerate this.

---

## Read this before you write any code

- The file has **382 rows** (students who took both subjects) and **61 columns**.
- There are **0 missing values**. The file is already clean - do not clean it again.
- **Columns that exist in both subjects carry a `_mat` or `_por` suffix.** There is no plain `G3` column. Use `G3_mat` or `G3_por`.
- The 13 **merge keys** have no suffix, because they are identical in both subjects by definition.
- Ordinal survey scales (1-5) are stored as integers so they can be used in correlations. Treat them as ordered categories when interpreting.

### Loading the data

```python
import pandas as pd

# Local (running from the repo root)
df = pd.read_csv('data/clean/student_clean.csv')

# Google Colab - pulls straight from GitHub, no upload needed
URL = 'https://raw.githubusercontent.com/<OWNER>/<REPO>/main/data/clean/student_clean.csv'
df = pd.read_csv(URL)
```

---

## Columns

| # | Column | Type | Role | Values / Range | Description |
|---|--------|------|------|----------------|-------------|
| 1 | `school` | str | MERGE KEY | GP, MS | School attended: GP = Gabriel Pereira, MS = Mousinho da Silveira |
| 2 | `sex` | str | MERGE KEY | F, M | Student sex: F = female, M = male |
| 3 | `age` | int64 | MERGE KEY | 15 to 22 | Student age in years |
| 4 | `address` | str | MERGE KEY | R, U | Home address type: U = urban, R = rural |
| 5 | `famsize` | str | MERGE KEY | GT3, LE3 | Family size: LE3 = 3 or fewer, GT3 = more than 3 |
| 6 | `Pstatus` | str | MERGE KEY | A, T | Parents' cohabitation status: T = together, A = apart |
| 7 | `Medu` | int64 | MERGE KEY | 0 to 4 | Mother's education: 0=none, 1=primary(4th), 2=5th-9th, 3=secondary, 4=higher |
| 8 | `Fedu` | int64 | MERGE KEY | 0 to 4 | Father's education: 0=none, 1=primary(4th), 2=5th-9th, 3=secondary, 4=higher |
| 9 | `Mjob` | str | MERGE KEY | at_home, health, other, services, teacher | Mother's job: teacher, health, services, at_home, other |
| 10 | `Fjob` | str | MERGE KEY | at_home, health, other, services, teacher | Father's job: teacher, health, services, at_home, other |
| 11 | `reason` | str | MERGE KEY | course, home, other, reputation | Reason for choosing this school: home, reputation, course, other |
| 12 | `guardian_mat` | str | attribute | father, mother, other | Student's guardian: mother, father, other  [Mathematics] |
| 13 | `traveltime_mat` | int64 | attribute | 1 to 4 | Home-to-school travel time: 1=<15min, 2=15-30min, 3=30-60min, 4=>60min  [Mathematics] |
| 14 | `studytime_mat` | int64 | attribute | 1 to 4 | Weekly study time: 1=<2h, 2=2-5h, 3=5-10h, 4=>10h  [Mathematics] |
| 15 | `failures_mat` | int64 | attribute | 0 to 3 | Number of past class failures (n if 1<=n<3, else 4)  [Mathematics] |
| 16 | `schoolsup_mat` | str | attribute | no, yes | Extra educational support from school: yes / no  [Mathematics] |
| 17 | `famsup_mat` | str | attribute | no, yes | Family educational support: yes / no  [Mathematics] |
| 18 | `paid_mat` | str | attribute | no, yes | Extra paid classes in this subject: yes / no  [Mathematics] |
| 19 | `activities_mat` | str | attribute | no, yes | Extra-curricular activities: yes / no  [Mathematics] |
| 20 | `nursery` | str | MERGE KEY | no, yes | Attended nursery school: yes / no |
| 21 | `higher_mat` | str | attribute | no, yes | Wants to take higher education: yes / no  [Mathematics] |
| 22 | `internet` | str | MERGE KEY | no, yes | Internet access at home: yes / no |
| 23 | `romantic_mat` | str | attribute | no, yes | In a romantic relationship: yes / no  [Mathematics] |
| 24 | `famrel_mat` | int64 | attribute | 1 to 5 | Quality of family relationships: 1=very bad to 5=excellent  [Mathematics] |
| 25 | `freetime_mat` | int64 | attribute | 1 to 5 | Free time after school: 1=very low to 5=very high  [Mathematics] |
| 26 | `goout_mat` | int64 | attribute | 1 to 5 | Going out with friends: 1=very low to 5=very high  [Mathematics] |
| 27 | `Dalc_mat` | int64 | attribute | 1 to 5 | Workday alcohol consumption: 1=very low to 5=very high  [Mathematics] |
| 28 | `Walc_mat` | int64 | attribute | 1 to 5 | Weekend alcohol consumption: 1=very low to 5=very high  [Mathematics] |
| 29 | `health_mat` | int64 | attribute | 1 to 5 | Current health status: 1=very bad to 5=very good  [Mathematics] |
| 30 | `absences_mat` | int64 | attribute | 0 to 75 | Number of school absences  [Mathematics] |
| 31 | `G1_mat` | int64 | attribute | 3 to 19 | First period grade (0-20)  [Mathematics] |
| 32 | `G2_mat` | int64 | attribute | 0 to 19 | Second period grade (0-20)  [Mathematics] |
| 33 | `G3_mat` | int64 | attribute | 0 to 20 | FINAL grade (0-20) - the primary target variable  [Mathematics] |
| 34 | `guardian_por` | str | attribute | father, mother, other | Student's guardian: mother, father, other  [Portuguese] |
| 35 | `traveltime_por` | int64 | attribute | 1 to 4 | Home-to-school travel time: 1=<15min, 2=15-30min, 3=30-60min, 4=>60min  [Portuguese] |
| 36 | `studytime_por` | int64 | attribute | 1 to 4 | Weekly study time: 1=<2h, 2=2-5h, 3=5-10h, 4=>10h  [Portuguese] |
| 37 | `failures_por` | int64 | attribute | 0 to 3 | Number of past class failures (n if 1<=n<3, else 4)  [Portuguese] |
| 38 | `schoolsup_por` | str | attribute | no, yes | Extra educational support from school: yes / no  [Portuguese] |
| 39 | `famsup_por` | str | attribute | no, yes | Family educational support: yes / no  [Portuguese] |
| 40 | `paid_por` | str | attribute | no, yes | Extra paid classes in this subject: yes / no  [Portuguese] |
| 41 | `activities_por` | str | attribute | no, yes | Extra-curricular activities: yes / no  [Portuguese] |
| 42 | `higher_por` | str | attribute | no, yes | Wants to take higher education: yes / no  [Portuguese] |
| 43 | `romantic_por` | str | attribute | no, yes | In a romantic relationship: yes / no  [Portuguese] |
| 44 | `famrel_por` | int64 | attribute | 1 to 5 | Quality of family relationships: 1=very bad to 5=excellent  [Portuguese] |
| 45 | `freetime_por` | int64 | attribute | 1 to 5 | Free time after school: 1=very low to 5=very high  [Portuguese] |
| 46 | `goout_por` | int64 | attribute | 1 to 5 | Going out with friends: 1=very low to 5=very high  [Portuguese] |
| 47 | `Dalc_por` | int64 | attribute | 1 to 5 | Workday alcohol consumption: 1=very low to 5=very high  [Portuguese] |
| 48 | `Walc_por` | int64 | attribute | 1 to 5 | Weekend alcohol consumption: 1=very low to 5=very high  [Portuguese] |
| 49 | `health_por` | int64 | attribute | 1 to 5 | Current health status: 1=very bad to 5=very good  [Portuguese] |
| 50 | `absences_por` | int64 | attribute | 0 to 32 | Number of school absences  [Portuguese] |
| 51 | `G1_por` | int64 | attribute | 0 to 19 | First period grade (0-20)  [Portuguese] |
| 52 | `G2_por` | int64 | attribute | 5 to 19 | Second period grade (0-20)  [Portuguese] |
| 53 | `G3_por` | int64 | attribute | 0 to 19 | FINAL grade (0-20) - the primary target variable  [Portuguese] |
| 54 | `absences_mat_capped` | int64 | DERIVED | 0 to 20 | absences_mat after IQR winsorisation (added by 01_data_prep.py) |
| 55 | `absences_por_capped` | int64 | DERIVED | 0 to 15 | absences_por after IQR winsorisation (added by 01_data_prep.py) |
| 56 | `G3_avg` | float64 | DERIVED | 0 to 18.5 | Mean of G3_mat and G3_por - overall performance (added) |
| 57 | `G3_diff` | int64 | DERIVED | -15 to 11 | G3_mat minus G3_por - positive = stronger at Mathematics (added) |
| 58 | `band_mat` | str | DERIVED | I (excellent/very good), II (good), III (satisfactory), IV (sufficient), V (fail) | Five-level grade band for G3_mat, Erasmus scale (added) |
| 59 | `band_por` | str | DERIVED | I (excellent/very good), II (good), III (satisfactory), IV (sufficient), V (fail) | Five-level grade band for G3_por, Erasmus scale (added) |
| 60 | `pass_mat` | int64 | DERIVED | 0 to 1 | 1 if G3_mat >= 10, else 0 (added) |
| 61 | `pass_por` | int64 | DERIVED | 0 to 1 | 1 if G3_por >= 10, else 0 (added) |

---

## Quick reference - the columns you will actually use

| Purpose | Column |
|---------|--------|
| Final Mathematics grade (main target) | `G3_mat` |
| Final Portuguese grade | `G3_por` |
| Earlier period grades | `G1_mat`, `G2_mat`, `G1_por`, `G2_por` |
| Absences | `absences_mat`, `absences_por` (capped versions available) |
| Study time | `studytime_mat`, `studytime_por` |
| Past failures | `failures_mat`, `failures_por` |
| Alcohol consumption | `Dalc_mat`, `Walc_mat`, `Dalc_por`, `Walc_por` |
| Wants higher education | `higher_mat`, `higher_por` |
| Mother's / father's job | `Mjob`, `Fjob` (no suffix - merge keys) |
| Grade band for count plots | `band_mat`, `band_por` |

---

## Source

Cortez, P., & Silva, A. (2008). *Using data mining to predict secondary school student performance.* In A. Brito & J. Teixeira (Eds.), Proceedings of 5th FUture BUsiness TEChnology Conference (pp. 5-12). EUROSIS.

Dataset: UCI Machine Learning Repository - Student Performance  
https://archive.ics.uci.edu/dataset/320/student+performance
