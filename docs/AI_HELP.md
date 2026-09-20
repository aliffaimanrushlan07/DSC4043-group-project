# Using AI help on this project

**From:** Aliff
**For:** Yasierul, Amir, Ramzi

Use AI freely for this. It's quicker than guessing. Below are the prompts that
work best, plus two technical traps that will silently break our report if you
hit them.

One thing to sort out first: check what DSC4043 actually permits for AI
assistance. Our brief says plagiarism will be penalised, and faculties differ.
Ask the lecturer if it isn't written down.

---

## What to attach

Just two files, every time:

1. your own `.py` file (`02_...`, `03_...` or `04_...`)
2. `docs/data_dictionary.md`

Not the whole zip. A zip sends the AI wandering into other people's files and
gives worse answers.

---

## Prompt 1 - Write the code

```text
I'm a student working on a data science assignment. Attached is my Python file
with # TODO markers, and the data dictionary for the dataset.

Help me complete TODO <n>. Show me the code and explain what each line does.

Rules:
- Only fill in this TODO. Don't restructure the file.
- The data is ALREADY CLEANED. Load student_clean.csv only. Never reload or
  re-clean student-mat.csv or student-por.csv.
- Use the exact column names from the data dictionary. There is no plain "G3"
  column - it's G3_mat or G3_por.
```

---

## Prompt 2 - Interpret your output

Run your code, then **upload the PNG or paste the numbers it printed**. Most AI
tools read images, so you can just drag the figure in.

```text
Here is the output from TODO <n> of my data science assignment.

<attach your PNG, or paste the printed numbers>

Context: dataset is 382 secondary school students from two Portuguese schools
(Cortez & Silva, 2008). Grades are on a 0-20 scale where 10 is a pass.
Columns ending _mat are Mathematics, _por are Portuguese.

Write me a 2-3 sentence interpretation suitable for a university report.
Include the actual numbers. Point out anything surprising, and say plainly
what this result does NOT prove.
```

That last sentence matters - the rubric rewards knowing the limits of a result,
and "correlation is not causation" is the specific thing markers look for.

If you want it sharper, follow up with:

```text
What's the most interesting thing in this output that I might have missed?
```

---

## Prompt 3 - Check it before you paste it in

```text
Check this interpretation against the output above. Is every number correct?
Have I claimed causation anywhere I only have correlation?
```

Worth 30 seconds. A number in the report that doesn't match what the code
printed is exactly what a marker spots.

---

## Two traps that will break our report

**Wrong column names.** An AI without the data dictionary writes `df['G3']` and
your script crashes with a `KeyError`. Harmless - you'll see it instantly.

**Re-cleaning the data.** This is the dangerous one. A "helpful" AI may add code
that reloads the raw CSVs and merges them again inside *your* script. It runs
without error and silently gives you a different number of students than
everyone else. Our report then contains contradictory figures and nobody notices
until marking.

**If your script mentions `student-mat.csv` or `student-por.csv` anywhere, that's
a bug. Delete it and tell me.** Only `01_data_prep.py` touches the raw files.

---

## Two things to keep in your own hands

**Read the interpretation before you paste it in.** If it says something you
don't actually believe about your own chart, change it. I'm assembling four
sections into one report, and four different voices is visible.

**Your Individual Reflection - 40 marks, graded per person.** It asks for a real
challenge you hit and how you solved it. Easiest way to have one: keep a scratch
file this week and note anything that breaks. Two minutes a day, and your
reflection is half written by Friday.

---

## Before you say you're done

```bash
python src/0X_your_file.py
```

Must run start to finish with no errors, PNGs must appear in `figures/`, and the
checklist it prints at the end must show no `<-- STILL A TODO`.

Stuck for more than 20 minutes? Message the group. That's what the daily
check-in is for.
