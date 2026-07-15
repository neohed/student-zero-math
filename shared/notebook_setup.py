"""
Shared notebook setup — call setup() at the top of any notebook.
Injects math CSS (KaTeX + MathJax fallback) and utility styles.
"""

from IPython.display import display, HTML

_MATH_CSS = """
<style>
/* ── Math rendering: KaTeX (VS Code) + MathJax (JupyterLab) ─────────── */
.katex, .MathJax {
    font-size: 1.65em !important;
    line-height: 1.4 !important;
}

/* Display (centred) equations — extra breathing room */
.katex-display, .MathJax_Display {
    margin: 1.8em 0 !important;
    padding: 0.6em 0 !important;
}

/* Deep blue: easier on the eye than default black */
.katex {
    color: #1e3a8a;
}

/* ── Term-highlight helpers (use in Markdown cells) ─────────────────── */
/* Example: <span class="hl-red">x</span>                               */
.hl-red   { color: #e11d48; font-weight: bold; }
.hl-blue  { color: #2563eb; font-weight: bold; }
.hl-green { color: #15803d; font-weight: bold; }
.hl-gold  { color: #b45309; font-weight: bold; }

/* ── Code blocks inside markdown ─────────────────────────────────────── */
.jp-RenderedHTMLCommon code,
.cell-output-text code {
    font-size: 0.95em;
}
</style>
"""


def setup():
    """Apply shared notebook styles. Call once in the first code cell."""
    display(HTML(_MATH_CSS))
