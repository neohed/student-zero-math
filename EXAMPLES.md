# Designing Examples

*How this repo builds examples that teach structure, not just cases.*

---

## Why This Exists

A notebook can be correct, comprehensive, and well-explained, and still teach badly — if the examples are the kind you forget five minutes after reading them. This doc exists because "intuition before notation" and "programmer bridges" (see [CLAUDE.md](./CLAUDE.md)) describe *what* an example should connect to, but not *how to design a sequence of examples* that actually gets a concept to stick.

The goal is not to give the reader a definition and then decorate it with a few worked cases. The goal is to let the reader *discover* the structure of a concept by noticing what stays the same and what changes across a carefully built sequence — then name it formally only once they've already half-figured it out.

This is [Variation Theory](https://en.wikipedia.org/wiki/Variation_theory), adapted for a solo programmer working through a Jupyter notebook, alone, with code.

---

## The Core Idea: Vary One Thing, Hold the Rest Still

Experts underestimate how hard a concept was to learn, because they no longer see the structure — they just see the answer. This is expert blind spot, and it's why a well-meaning explanation ("a derivative is the instantaneous rate of change") often lands as noise to someone who hasn't yet built the concept.

The fix is not to explain harder. It's to **let the pattern become visible through contrast**:

- **Separation** — vary one dimension at a time (change only the exponent, only the sign, only the starting value) so the reader can isolate what that dimension actually controls.
- **Contrast** — put a strong non-example next to a real example, so the boundary of the concept becomes visible, not just its interior.
- **Generalization** — show the same structure in a new surface (a new domain, a new data shape, a new context) to prove it wasn't a coincidence of the first example.
- **Fusion** — once the separate dimensions have each been seen alone, vary more than one at once, so the reader sees them interact.

A good example sequence in this repo moves through these in roughly that order: separate, contrast, generalize, fuse. The formal definition or formula shows up only at the end, as the compact name for a pattern the reader has already recognized.

---

## The Two Reps That Aren't Optional

Generic example design (comparison, non-examples, multiple representations) is well-established pedagogy. This repo adds two constraints on top of it, both grounded in [PHILOSOPHY.md](./PHILOSOPHY.md), and both non-negotiable for every example sequence written here.

### 1. Code is a representation, not a bonus

"Multiple representations" usually means concrete/visual/tabular/graphical/symbolic. In this repo, **the code representation is mandatory, and it often carries more weight than the symbolic one** — because a `for` loop or an array reshape is a structure the reader already owns. Every example needs a version the reader can run, not just read.

Concretely: when showing a summation, don't just also write a for-loop as an aside — make the for-loop and the $\sum$ two labels for the same object, shown side by side, so that varying one dimension in the code (the loop bound) and watching the symbolic form respond is itself part of the "separation" step.

### 2. Lead with the living thing

PHILOSOPHY.md's second McGilchrist insight: the right hemisphere attends to novelty, motion, and complexity before the left hemisphere can categorize anything. Comparing static examples side-by-side ("what's the same in 1–4?") is valuable, but it is fundamentally left-hemisphere work — pattern-matching across things already laid out flat. It only works well once the reader's attention has actually been captured.

So: **before the comparison sequence starts, the first thing the reader sees should move.** An animation, a slider, a plot that updates as a parameter changes. Not as a hook bolted onto the intro — as the first example in the sequence, the thing that makes the reader curious enough to want to know why it behaves that way. The static, carefully-varied examples that follow are answering a question the living example already raised.

---

## Non-Examples Should Be Buggy Code

Generic guidance says "include a non-example so the boundary is visible." For this audience, the sharpest non-example is usually **the code a programmer would instinctively write, and the specific way it's wrong** — not a mathematical near-miss.

- An off-by-one loop bound that computes the wrong number of terms
- A broadcasting mismatch that silently produces the wrong shape instead of erroring
- A reduction along the wrong axis that runs fine and returns nonsense
- A recursive function missing a base case

These land harder than "here's a non-triangle" because the reader has probably shipped that exact bug before. Where possible, pair the buggy version and the correct version as running code, side by side, and let the reader spot the difference before you point to it.

---

## Formulas Are a Contrast Case Too

PHILOSOPHY.md's permutation example — $P(n,r) = \frac{n!}{(n-r)!}$ simplifying to a bounded countdown loop — is already a variation-theory move: naive execution vs. algebraic manipulation, revealing that the "formula" and the "loop" were the same object all along.

Treat this as a repeatable pattern of variation, not a one-off aside specific to combinatorics:

> **Example (naive):** compute the formula as written — plug in values, get an answer, no insight.
> **Example (manipulated):** expand, cancel, rearrange — reveal the structure a programmer would recognize.

Use this contrast pair wherever a formula in the notebook has an opaque closed form that conceals a loop, a recurrence, or a simpler identity. It's frequently the single most valuable example in a notebook, and it's easy to skip if you go straight from formula to application.

---

## Example Sequence Template

For any concept getting its own worked-example section, build roughly this shape. Not every step needs its own numbered example — several can share one code cell — but don't skip a step.

1. **Critical aspects to discern** — before writing any examples, write down 3–6 things the reader must notice: what stays invariant, what's a common bug, what the edge cases are. This list drives which dimensions you vary later. Keep it out of the final notebook; it's a design tool, not reader-facing content.
2. **The living example** — one animation, interactive slider, or dynamically-updating plot the reader can play with before anything is explained. This is example 1, always.
3. **Separation** — 2–4 examples, each varying exactly one dimension identified in step 1, shown in both code and symbolic form.
4. **Contrast** — at least one strong non-example: buggy code, a boundary case, or a case that looks similar but fails. Put it directly beside the working version.
5. **Generalization** — 1–2 examples that show the same structure in a different surface (new domain, new data shape, new context) to prove the pattern wasn't a coincidence.
6. **Fusion** — 1–2 examples that vary more than one dimension at once, now that the reader has seen each dimension alone.
7. **Naming the pattern** — only now, introduce the formal notation or definition, framed explicitly as the compact name for what the reader has already seen work.

---

## Guiding Prompts for a Solo Reader

This repo has no live instructor and no classroom to compare answers in. Replace "ask students to discuss" with a **direct prompt to the reader in a markdown cell, followed by a code cell they're invited to run or modify, followed by a later cell that names the pattern.** The gap between the prompt and the reveal is where the learning happens — don't collapse it.

Useful prompt shapes:

- "Before running the next cell — what do you expect to happen if [dimension] increases? Try it."
- "What's the same between the last two examples? What changed?"
- "This code looks like it should work. Run it. What actually happened, and why?"
- "Here's the formula. Before evaluating it, try to simplify it by hand — what does it reduce to?"

Keep these short and specific to the dimension currently being varied — a vague "what do you notice?" is easy to skim past; a pointed prediction question is not.

---

## What to Avoid

- Starting an example sequence with the formal definition or formula — even a brief one. If notation shows up before example 7 in the template above, it went in too early.
- A sequence of examples that only varies surface numbers (changing 3 to 7) without varying a structural dimension (sign, shape, boundary condition, direction).
- Comparison prompts with no living/interactive example before them.
- Non-examples that are just "a different math object" rather than a bug a programmer would actually write.
- Treating this doc as a checklist to satisfy rather than a sequence to actually design — six examples that technically hit every step but don't build on each other are worse than four that do.

---

*Examples are not decoration for an explanation. They are how the explanation gets built.*
