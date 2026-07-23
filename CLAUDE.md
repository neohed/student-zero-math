# CLAUDE.md — Project Briefing

This file is read by Claude Code at the start of every session. It contains everything needed to work on this repo without prior context.

---

## What This Project Is

**`student-zero-math`** is a personal learning resource — a library of Jupyter notebooks and small Python projects covering mathematics and AI research, written for programmers with no formal math background.

The author is [@neohed](https://github.com/neohed) — a software engineer with 26 years of experience and a CS & AI degree, learning math in the open.

The guiding principle is the **Feynman Technique**: writing clear explanations for others forces genuine understanding. The author is student zero. Everything is written as if explaining to a smart, experienced programmer who is new to the topic.

Full philosophy: [PHILOSOPHY.md](./PHILOSOPHY.md)
How to design examples: [EXAMPLES.md](./EXAMPLES.md)
How to review a notebook: [REVIEW.md](./REVIEW.md)

---

## Target Audience

**Programmers who lack formal math training.** Specifically:

- Experienced developers, not beginners
- Comfortable with abstraction, functions, iteration, recursion
- No assumed math knowledge beyond basic arithmetic
- Smart adults who respond to honesty and precision, not hand-holding

This is an engineering resource, not an academic one. The tone is direct, clear, and practical.

---

## Core Content Rules

These rules apply to every notebook and document in this repo:

1. **Intuition before notation** — always build the concept in plain English and code before introducing formal math symbols
2. **Programmer bridges** — connect every new concept to something the reader already knows from programming (a summation is a for loop, a matrix is a 2D array, etc.)
3. **No hand-waving** — if something is complex, slow down and explain it; never skip over hard parts
4. **Theory followed by implementation** — every concept must have working code; math without code is incomplete here
5. **PoC required** — every research paper companion must include at least one standalone proof-of-concept project, not just a notebook
6. **Feynman standard** — if an explanation is unclear, it means the concept is not understood well enough yet; rewrite until it is clear
7. **Engineer's voice** — practical, direct, curious; never academic, never condescending

---

## Tech Stack

- **Python**: 3.12.3
- **Notebooks**: Jupyter (`.ipynb`), authored in VS Code
- **Package manager**: pip (requirements.txt per project where needed)
- **Large models**: stored locally in `models/` (gitignored); downloaded via script, never committed
- **Key libraries**: NumPy, pandas, matplotlib, PyTorch, HuggingFace Transformers, vLLM (for PoC demos)

---

## Repo Structure

```
student-zero-math/
│
├── fundamentals/               # Math foundations, programmer's lens
│   ├── 01-pre-algebra-and-algebra/
│   ├── 02-calculus/
│   ├── 03-linear-algebra/
│   ├── 04-geometry-and-graphics/
│   ├── 05-complex-numbers-and-fractals/
│   └── 06-dynamical-systems/
│
├── books/                      # Companion notebooks for key texts
│   ├── math-for-programmers/
│   ├── no-bullshit-guide/
│   └── sutskever-list/         # One folder per paper
│       └── 01-paper-name/
│           ├── notebook.ipynb  # Explanation and worked examples
│           ├── README.md       # Paper context, link, why it matters
│           └── poc/            # Standalone PoC project(s)
│
├── tools/                      # Repo utilities (search, graph — future)
├── models/                     # Gitignored — large model files
├── shared/                     # Common utilities, plot styles
│
├── CLAUDE.md                   # This file
├── PHILOSOPHY.md               # Teaching philosophy
├── README.md                   # Public-facing overview
├── .gitignore
└── .gitattributes
```

---

## Notebook Structure Convention

Each notebook should follow this structure:

1. **Title and introduction** — what this notebook covers and why it matters
2. **Prerequisites** — what the reader needs to know (kept minimal)
3. **Intuition first** — plain English explanation, programmer analogies
4. **Worked examples** — concrete, runnable code that demonstrates the concept
5. **Visualisation** — where applicable, plot it; visual understanding matters
6. **Exercises** — invite the reader to experiment and modify
7. **Formal notation** — introduce math symbols after intuition is established
8. **Real-world connection** — what can you build with this?
9. **Summary** — key takeaways in plain English

---

## Shared Helper Code Convention

When a notebook introduces a helper function that a *later* notebook will also need (e.g. `poly_str`, `mono_str`, `factor_gcf`):

- Write it **inline, in the notebook that first teaches it** — the code itself is part of the lesson (e.g. notebook 15's `poly_str` is the proof that "a polynomial is a dict"). Do not hide teaching code behind an import.
- Also add it to the matching file in `shared/` (e.g. `shared/polynomials.py`) as the canonical, single source of truth.
- Every **later** notebook that reuses that helper imports it from `shared/` rather than re-pasting it:
  ```python
  import sys
  sys.path.insert(0, '../..')  # repo root, so `shared` is importable
  from shared.polynomials import poly_str, poly_eval, poly_clean
  ```
  (Adjust the relative path if the notebook's folder depth differs from `fundamentals/<topic>/`.)
- If a bug is found in a helper, fix it once in `shared/`, then update the one inline teaching copy to match. Never fix only one copy and leave others silently out of sync — check for other files that reuse the same helper.
- Before writing any function meant to be reused, run `view` on `shared/polynomials.py` (or the matching shared file) and read its docstring index first — do not rely on memory of what already exists.
- A notebook's own new-for-this-lesson helpers stay inline, not imported, even if they will later be added to `shared/` for the next notebook to reuse.

---

## PoC Project Convention

Each PoC in `poc/` should:

- Be a small, self-contained Python project
- Do something real and demonstrable — not a toy example
- Include a `README.md` explaining what it does and how to run it
- Include a `requirements.txt` if it has dependencies
- Be runnable with a single command where possible

---

## What To Avoid

- Academic tone or style
- Explaining notation before building intuition
- Skipping over hard parts with "it can be shown that..."
- Notebooks that are all explanation with no runnable code
- PoCs that are just notebook code extracted into a `.py` file — they should demonstrate something real
- Overly complex folder structures or over-engineering

---

## Session Notes

- Check `PHILOSOPHY.md` if uncertain about tone or approach
- Check `EXAMPLES.md` before writing worked examples for any concept — do not default to a plain worked-example list
- Run `/review-notebook` before considering a new notebook finished, or when it depends on an older one
- When creating a new notebook, follow the notebook structure convention above
- When creating a new paper companion, create the full folder structure: `notebook.ipynb`, `README.md`, and `poc/` placeholder
- Prefer clear and simple over clever
- If something feels academic, rewrite it

---

*Clarity over cleverness.*
