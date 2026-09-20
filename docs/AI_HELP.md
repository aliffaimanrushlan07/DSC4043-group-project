# Using AI help on this project

**From:** Aliff
**For:** Yasierul, Amir, Ramzi

Getting help with Python syntax is fine and normal. This page is about doing it
in a way that doesn't cost you marks — because there are two specific ways it
can, and both are avoidable.

---

## First: check the rules

Our brief states that **any plagiarism will be penalised**. Different lecturers
and faculties treat AI assistance differently. Before you use it, check what
DSC4043 actually permits — ask the lecturer if it isn't written down anywhere.
Don't assume, and don't rely on what another group tells you.

---

## The part you must write yourself

Your **Individual Reflection is worth 40 marks, graded per person.** That is more
than your share of the entire group report. It asks for:

- what you contributed, with evidence
- **at least one technical or conceptual challenge you encountered, and how you solved it**
- what you learned about pandas, Matplotlib, Seaborn and statistics

If an AI wrote your section and you never hit a problem, you have nothing
truthful to put there. The rubric gives 1–5 for "vague, no evidence" and 6–10
for "clear, specific, with evidence" — and a marker can tell the difference.

The same goes for the `INTERPRETATION` strings in your script. Those become the
actual paragraphs in the report, and the visualisation rubric caps at 10/20 for
"weak explanation". **Write those yourself, after you have seen your own output.**
That is where the marks are, and it is the one part that is genuinely yours.

---

## If you do use AI, do it this way

**Don't upload the whole repository zip.** Attach only two files:

1. your own `.py` file (`02_...`, `03_...` or `04_...`)
2. `docs/data_dictionary.md`

Then paste this prompt:

```text
I'm a student working on a data science assignment. Attached is my Python
file with # TODO markers, and the data dictionary for the dataset.

Help me complete the TODOs ONE AT A TIME, not all at once. For each one:
  1. Explain what the code needs to do and why
  2. Show me the code
  3. Explain each line, so I can answer questions about it later

Rules:
- Only fill in the TODO sections. Do not restructure the file or change
  anything outside them.
- The data is ALREADY CLEANED. Load student_clean.csv only. Never reload or
  re-clean student-mat.csv or student-por.csv.
- Use the exact column names from the data dictionary. There is no plain
  "G3" column - it is G3_mat or G3_por.
- Do NOT write the INTERPRETATION text for me. I will write that myself
  after I see my own output.
```

The "one at a time" and "explain each line" parts matter. If you can't explain
what your own code does, you will not be able to write the reflection, and you
will not be able to answer if you're asked about it.

---

## Two traps to watch for

**Wrong column names.** An AI that doesn't have the data dictionary will write
`df['G3']` and your script will crash with a `KeyError`. That's the harmless
version.

**Re-cleaning the data.** This is the dangerous one. A "helpful" AI may add code
that reloads the raw CSVs and merges them again inside *your* script. It will
run without error, and it will silently give you a different number of students
than everyone else. Our report would then contain contradictory figures and
nobody would spot it until marking.

**If your script contains `student-mat.csv` or `student-por.csv` anywhere, that
is a bug. Delete it and tell Aliff.** Only `01_data_prep.py` touches the raw files.

---

## The check before you say you're done

```bash
python src/0X_your_file.py
```

It must run start to finish with no errors, your PNGs must appear in `figures/`,
and the checklist it prints at the end must show no `<-- STILL A TODO`.

And one more, for yourself: **can you explain every line you're submitting?**
If not, go back and work through it until you can. Stuck? Message the group —
that's what the daily check-in is for, and a real question you asked is
much better reflection material than a problem you never had.