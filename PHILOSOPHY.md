# Teaching Philosophy

*by [@neohed](https://github.com/neohed)*

---

## Why This Exists

I have a CS & AI degree and 26 years of experience as a software engineer. I am not a mathematician. But I want to be better at math — and I want to understand AI at a deeper level, where math fluency matters.

So I built this resource for myself first. I am **student zero**.

The working hypothesis is that the best way to learn something deeply is to teach it. Writing clear explanations forces you to find the gaps in your own understanding. Explaining to a hypothetical reader — even an imaginary one — holds you to a higher standard than private notes ever will. This is the **Feynman Technique**, and it is the foundation of everything in this repo.

If it helps others along the way, that is a bonus worth having.

---

## Who This Is For

This resource is written for **programmers who lack formal math training**.

Not beginners. Not academics. Programmers — people who:

- Already think in abstractions, functions, loops, and transformations
- Are comfortable with "let's try it and see"
- Can verify understanding by implementing something and running it
- Think in systems, inputs, outputs, and edge cases

If you're a programmer who'd like to be better at math, this might help.

---

## The Core Idea: Use What You Already Know

Programmers have rich mental models that map directly onto mathematical concepts. The goal is to make those connections explicit — to show that the math is often just a more precise, compact way of expressing something you already understand in code.

Some examples of how this works:

- A **mathematical function** is just a function in code — same idea, same rules
- A **summation** $\sum$ is a for loop that accumulates a result
- A **matrix** is a 2D array with well-defined rules for combination
- A **derivative** is "how much does the output change when I nudge the input slightly"
- **Solving for x** is finding the input that makes an assertion true — like a unit test that must pass
- An **equation** is an assertion that two expressions are equal

The notation comes second. Always. We build the intuition first in terms you already own, then introduce the formal notation as a reward — a compact, precise way of writing what we have already understood.

---

## Why This Approach Works — The Neuroscience

The teaching methods in this repo are not arbitrary. They are grounded in how the brain actually processes and retains new information, drawing on the work of psychiatrist and neuroscientist Iain McGilchrist.

Two insights from McGilchrist are particularly relevant here.

**Insight 1 — Knowledge agglomerates.**

We do not learn new things in isolation. The brain builds new understanding by attaching it to existing structures — new knowledge needs somewhere to land. This is why abstract concepts introduced without context evaporate, while the same concepts introduced through familiar analogies stick.

For programmers learning math, this means the programmer bridge is not just a convenience — it is how learning actually works. When we show that a summation $\sum$ is a for loop, or that solving for $x$ is like finding the input that passes a unit test, we are giving new knowledge a secure anchor in a structure the brain already owns. The math has somewhere to attach. It does not float unmoored in working memory and fade.

This is also why the series structure of this repo matters. Each notebook builds on the last. Each new concept is introduced in relation to something already understood. The curriculum spirals — returning to familiar ground, each time from a higher vantage point.

**Insight 2 — The right hemisphere attends to aliveness first.**

McGilchrist's research shows that the right hemisphere of the brain attends first to novelty, complexity, and what he calls *aliveness* — a broader category than biological life. It includes anything that moves, flows, emerges, or behaves. The right hemisphere opens the door. The left hemisphere — which handles categorisation, analysis, and formal symbol manipulation — can only do its work once the right hemisphere has attended and signalled: *something is happening here.*

This has a direct implication for how we teach: **lead with the living thing**.

A bouncing ball that decays to rest, a curve being drawn in real time, a system responding dynamically to a slider — these are alive in McGilchrist's sense. They are complex, emergent, flowing. They engage the right hemisphere before the left hemisphere knows what's happening. The formal explanation then arrives into an already-engaged, already-curious brain. This is far more effective than leading with notation and following up with a demo.

This is why every notebook in this repo leads with a running animation before introducing any formula. It is why interactive sliders are a pedagogical essential, not a cosmetic feature. It is why visual richness — trails, dynamic plots, colour — is not decoration but function.

**The practical rules that follow from this:**

- Show the living, moving, complex thing first — before any explanation
- Use animation and interactive sliders in every notebook where possible
- Let the right hemisphere attend before asking the left hemisphere to analyse
- Build every concept on top of something already known — never introduce in isolation
- The spiral curriculum is not just good practice — it is how the brain works

---

## Formulas Are Code to Write, Not Code to Run

This is one of the most common and least-discussed sources of confusion for programmers learning math.

When a programmer sees a formula, the instinct is to *execute* it — plug in the values, get the answer. A formula looks like a finished function call. You pass in the arguments, it returns the result. Done.

**That instinct is wrong — and it causes real confusion.**

A formula is not a finished program. It is a starting point. In mathematics, the full solution includes the algebraic steps that follow — simplification, expansion, cancellation, rearrangement. Those steps are not bookkeeping. They are where the insight lives.

> **Using math is like writing code, not running code.**

The mathematician's instinct when they see a formula is not to evaluate it — it is to *manipulate* it. Simplify it. Expand it. Cancel terms. Rearrange it until it reveals its structure. This is the same instinct a good programmer has when refactoring: you do not just run messy code, you clean it up until it says what it actually means.

**A concrete example:**

The formula for permutations — selecting $r$ items from $n$ without repetition — is:

$$P(n, r) = \frac{n!}{(n-r)!}$$

A programmer's instinct: compute $n!$, compute $(n-r)!$, divide, done. Correct answer, zero insight.

The mathematician's instinct: simplify. Expand the factorials and cancel:

$$\frac{n!}{(n-r)!} = \frac{n \times (n-1) \times \cdots \times (n-r+1) \times \cancel{(n-r)!}}{\cancel{(n-r)!}} = n \times (n-1) \times \cdots \times (n-r+1)$$

What remains is a product that counts down from $n$, stopping after $r$ steps. Which is exactly the bounded loop a programmer would write instinctively:

```python
result = 1
for i in range(n, n - r, -1):
    result *= i
```

The division was never really there. It was a compact way of expressing a bounded product — and the simplification revealed that. **The formula and the loop are the same thing.** But you only see that if you do the algebraic work.

This pattern recurs throughout mathematics. Formulas that look complex often simplify to something a programmer would recognise immediately. The simplification is not a side step — it is the point.

When you encounter a formula that feels opaque: do not just evaluate it. Manipulate it. The insight is usually in the simplified form.

## Math as a Tool, Not an End

This is an **engineering resource**, not an academic one.

Every concept covered here has a practical application. Theory is always followed by a working proof-of-concept — real code, running in the real world, doing something useful. Not toy examples for their own sake, but small demonstrations that show what the math actually enables.

The question we always ask is: *what can you build with this?*

---

## The Feynman Standard

Every notebook in this repo is written as if explaining to a smart person who is new to the topic. This means:

- No assumed knowledge beyond programming fundamentals
- No hand-waving over the hard parts
- If something is complex, we slow down — we do not skip
- Formal notation is introduced after intuition is established, never before
- If I cannot explain it clearly, I do not understand it well enough yet

This standard applies equally to the fundamentals series and the research paper companions. A paper on transformer architecture should be as accessible as a notebook on algebra, given the right scaffolding.

---

## Structure of This Repo

The repo is organised into three areas:

**`fundamentals/`** — Mathematical foundations built from the ground up. Pre-algebra, algebra, calculus, linear algebra, geometry, complex numbers, dynamical systems. Each topic approached through the programmer's lens.

**`books/`** — Companion notebooks for key texts. Includes a companion series for *Sutskever's List* (a curated collection of landmark AI research papers) and other books that bridge math and programming. Each paper or chapter gets its own folder containing at minimum a notebook and a working PoC project.

**`tools/`** — Utilities for working with the repo itself. Planned: a search tool, possibly backed by a vector store, to navigate content semantically across notebooks.

---

## Proof-of-Concept Projects

Each research paper companion includes at least one small standalone project — a PoC that implements or demonstrates the core idea of the paper in working code.

These are not polished production applications. They are **engineer's sketches** — enough to prove the concept works, understand how it behaves, and build intuition that reading alone cannot provide.

Theory without implementation is incomplete. We build things here.

---

## A Living Resource

This repo is a work in progress and always will be. Topics are added as I study them. Notebooks are revised as my understanding deepens. The Feynman Technique guarantees that revision is part of the process — finding out you explained something badly is how you find out you did not understand it well enough.

Contributions, corrections, and questions are welcome.

---

*Built with curiosity, maintained with honesty.*
