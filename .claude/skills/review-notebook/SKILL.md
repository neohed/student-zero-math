---
name: review-notebook
description: Audit a notebook (new or existing) for code duplication, correctness, and pedagogy against current repo standards. Use before considering a new notebook finished, or when a new notebook depends on an older one.
---

# Review Notebook

Target notebook or notebook set is given in `$ARGUMENTS`. Follow these steps **in order** — each is an action, not a reminder:

1. **View the shared index.** Run `view` on the relevant `shared/*.py` file (e.g. `shared/polynomials.py`) and read its module docstring, which lists every helper and which notebook teaches it. Do this before step 2 — do not judge duplication or invention from memory.
2. **View the target notebook's full source.**
3. **Cross-check every function defined in the notebook against the shared index from step 1.** For each: is it (a) correctly imported because it was taught earlier, (b) correctly inline because it's taught here for the first time, or (c) a duplicate/near-duplicate of something already in the index under a different name? Flag every case of (c) explicitly, including near-misses (same purpose, different signature or name).
4. **Scan the notebook's own code cells for repeated inline logic** — the same formatting/computation expression written by hand more than once across different functions in this notebook. Flag each instance.
5. **Check for dead code** — anything imported or defined but never called.
6. **Execute the notebook end-to-end** (or the relevant cells if full execution isn't practical) and confirm zero errors and that every verification print states success.
7. **Report findings before fixing anything** — list what was found in steps 3–6, grouped by cross-notebook duplication / reinvented helper / in-notebook duplication / dead code / execution failure. Wait for confirmation on which to fix, unless the person has already said to fix everything found.
8. **If doing the pedagogy pass too:** apply the EXAMPLES.md checklist from REVIEW.md's Pass 2 to the notebook's example sections, and report separately from the code-hygiene findings.

Never skip step 1 — reinvented helpers happen specifically when a new function is written without checking what already exists.
