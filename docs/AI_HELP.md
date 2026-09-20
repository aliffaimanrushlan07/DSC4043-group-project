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
- Help me to interpret result for every plot when i upload the result such as image/screenshots/pasted results
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