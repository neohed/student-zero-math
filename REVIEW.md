# Reviewing Notebooks

*Checklist for auditing a notebook — new or old — against current repo standards.*

Two separate passes: **code hygiene** (is it correct and non-duplicated) and **pedagogy** (does it teach well per [EXAMPLES.md](./EXAMPLES.md)). A notebook can pass one and fail the other — check both.

---

## Pass 1: Code Hygiene

1. **Read the index first.** View `shared/polynomials.py` (or the matching shared file for this topic) before judging anything — know what already exists before flagging something as missing or duplicated.
2. **Cross-notebook duplication.** Does this notebook re-paste a helper that's taught in an earlier notebook, instead of importing it from `shared/`? (See CLAUDE.md's Shared Helper Code Convention.)
3. **Reinvented helpers.** Does this notebook define something under a new name that already exists in `shared/` under a different name? Check signatures, not just names — `mono_str(coeff, exp)` and `mono_str(coeff, exp, var='x')` are the same collision even if one has an extra default arg.
4. **In-notebook duplication.** Within this notebook's own code cells, is the same formatting/logic expression written out more than once by hand (e.g. a term-formatting `if/else` repeated across several display functions)? If a shared helper covers it, use that; if it's genuinely local, factor it into one local function.
5. **Dead code.** Any helper defined or imported but never called in this notebook?
6. **Execute end-to-end.** Run every cell in order. Zero errors. Every `verify`/`check` print should say OK — if one doesn't, the notebook is wrong, not just messy.
7. **Sync with canonical source.** If this notebook has an inline "taught here" copy of a helper that also lives in `shared/`, confirm they're character-for-character identical. A bug fixed in one and not the other is worse than never having deduplicated at all.

## Pass 2: Pedagogy

Apply [EXAMPLES.md](./EXAMPLES.md)'s sequence to the notebook's worked-example section(s):

1. Is there a living/interactive example before any static comparison?
2. Are examples separated one dimension at a time before being combined?
3. Is there at least one non-example, and is it a buggy-code shape rather than a pure math near-miss?
4. Does formal notation appear only after the pattern has already been demonstrated?
5. Do guiding prompts ask the reader to predict before revealing, rather than "what do you notice?"

If a notebook fails Pass 2 but passes Pass 1, it's not broken — it's just from before EXAMPLES.md existed. Note it, don't necessarily rewrite it on the spot (see CLAUDE.md's review-trigger policy: rewrite when a new notebook actually depends on it, not on a schedule).

---

## When to Run This

- Before considering a **new** notebook finished.
- When a **new** notebook cites an old one as a prerequisite or imports its helpers (the old one gets pulled into scope anyway — check it while you're there).
- Not on a fixed schedule across the whole repo — see CLAUDE.md.
