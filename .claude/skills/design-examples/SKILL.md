---
name: design-examples
description: Redesign or build the worked-example sequence for a concept or notebook section, following EXAMPLES.md step by step. Use when a notebook's examples feel generic, disconnected, or like they were skipped past rather than deliberately sequenced.
---

# Design Examples

Apply the process in [EXAMPLES.md](../../../EXAMPLES.md) explicitly and in order to the concept or section given in `$ARGUMENTS`. Do not skip ahead to writing worked examples directly.

Steps to follow, in this order:

1. Identify the concept or notebook section this applies to. If it's an existing notebook, read the relevant section first.
2. Write out the **critical aspects to discern** for this concept (3–6 things the reader must notice — invariants, common bugs, edge cases). This is a design note; it does not go in the notebook itself.
3. Design **the living example** — one animation, interactive slider, or dynamically-updating plot the reader engages with before any explanation. This is always example 1.
4. Design the **separation** examples — 2–4 examples, each varying exactly one critical aspect at a time, each shown in both code and symbolic form.
5. Design at least one **contrast / non-example** — for this audience, prefer buggy code a programmer would actually write (off-by-one, wrong axis, missing base case) over a purely mathematical near-miss.
6. Design the **generalization** examples — 1–2 examples showing the same structure in a different surface (new domain, new data shape, new context).
7. Design the **fusion** examples — 1–2 examples that vary more than one critical aspect at once.
8. Only now, write the **formal notation or definition**, framed explicitly as the compact name for the pattern already demonstrated.
9. Write the **guiding prompts** for the solo reader — direct, specific prediction questions placed before each reveal, not generic "what do you notice" prompts.

If the target concept involves a formula with a non-obvious closed form (e.g. combinatorics, series), include the naive-execution-vs-algebraic-manipulation contrast pair described in EXAMPLES.md, in addition to the buggy-code non-example.

When done, present the sequence in the notebook's standard structure (see CLAUDE.md's Notebook Structure Convention) rather than as a flat, undifferentiated list of examples.
