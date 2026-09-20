# Using AI assistance on this project

**DSC4043 Group Project | Read this before you ask ChatGPT, Claude or anything else for help.**

---

## First: check the rules

Our brief states that **any plagiarism will be penalised**. Universities differ on what AI assistance is allowed, and none of us should assume. **Check the module's policy or ask the lecturer directly** before you rely on an AI for any part of this.

What follows assumes assistance is permitted for learning and debugging. It is not permission — it's guidance for staying on the right side of the line if it is.

---

## The line that matters

There are two different things in your `.py` file, and they are not equally safe to get help with.

**Code TODOs** — `# TODO 1:`, `# TODO 2:` and so on.
Getting help with syntax is ordinary. Everyone looks up how `groupby` works. Just make sure you understand the code you end up with, because you'll need to explain it.

**Writing TODOs** — the `INTERPRETATION` strings.
**Write these yourself.** They are the actual marks. The rubric awards up to 20 for visualisation but caps at 10 for "few plots, weak explanation." The plots are the easy half; the explanation is what's being paid for. An AI writing your interpretation is the part that is both academically risky and costs you marks, because it will produce something generic that any marker has read a hundred times.

---

## Your individual reflection is the real reason to care

**40 marks, graded per person** — more than your share of the group report. It requires:

- Your contribution, *with evidence*
- **At least one technical or conceptual challenge you encountered, and how you solved it**
- What you learned about pandas, Matplotlib, Seaborn and statistics
- How your work links to the CLO

If you paste a file into an AI and paste the answer back, you have nothing true to write in any of those four. The reflection rubric gives 1–5 for "vague, no evidence" and 6–10 for "clear, specific." Hollow work is visible there in a way it isn't in code.

The struggle *is* the deliverable. A bug you fought for an hour is worth 10 marks in your reflection. Don't trade that away for twenty minutes.

---

## Don't upload the whole repository

Two reasons, both practical:

1. An AI that can see `01_data_prep.py` may "helpfully" reload and re-clean the raw CSVs inside *your* script. That silently breaks our single-source-of-truth rule and puts a different row count in the report.
2. More context means more chances for it to rewrite things nobody asked it to touch.

**Upload only two files:** your own `.py`, and `docs/data_dictionary.md`.

---

## A prompt that works

Paste this, attach those two files:

> I'm a student working on a data science assignment. Attached is my Python file with `# TODO` markers, and the data dictionary for the dataset.
>
> Help me complete the TODOs **one at a time**, not all at once. For each one:
> 1. Explain what the code needs to do and why
> 2. Show me the code
> 3. Explain each line, so I can answer questions about it
>
> Rules:
> - Only fill in the TODO sections. Don't restructure the file or change anything else.
> - The data is already cleaned — load `student_clean.csv` only. Never reload or re-clean the raw CSVs.
> - Column names come from the data dictionary. There is no plain `G3` column — it's `G3_mat` or `G3_por`.
> - Don't write the `INTERPRETATION` text for me. I'll write that myself after I see the output.

The last two rules are the important ones.

---

## Check whatever you get back

AI-generated code is confident and sometimes wrong. Before you commit:

- [ ] `python src/0X_your_file.py` runs with **no errors**
- [ ] Your PNGs are in `figures/` and **actually show data** — open them and look
- [ ] Every number you quote in your write-up **came from your own output**, not from the AI's guess or from a hint comment
- [ ] Nothing outside your TODO sections changed
- [ ] The script still loads `student_clean.csv` and nothing else
- [ ] You can explain every line to Aliff without looking it up

That last one is the real test. If you can't explain it, you can't defend it in your reflection, and you shouldn't submit it.

---

## When you're stuck, message the group first

Seriously. Aliff built the data pipeline and is on call all week. A two-minute answer from him beats forty minutes of arguing with a chatbot that can't see our dataset — and "I asked a teammate and we worked it out" is a perfectly good story for your challenges section.
