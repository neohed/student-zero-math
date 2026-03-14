from fractions import Fraction
from math import gcd
from IPython.display import display, Markdown


def lcm(a: int, b: int) -> int:
    """Least common multiple (positive integers)."""
    return abs(a * b) // gcd(a, b)


def add_subtract_fractions(frac1: Fraction, frac2: Fraction, operation: str = "+"):
    d1, d2 = frac1.denominator, frac2.denominator
    common_den = lcm(d1, d2)

    # numerators with the common denominator
    n1 = frac1.numerator * (common_den // d1)
    n2 = frac2.numerator * (common_den // d2)

    # operation
    if operation == "+":
        result_num = n1 + n2
        op_sym = "+"
    elif operation == "-":
        result_num = n1 - n2
        op_sym = "-"
    else:
        raise ValueError("operation must be '+' or '-'")

    result = Fraction(result_num, common_den)

    # ----- LaTeX helpers -------------------------------------------------
    def tex_num(n):
        """Put a minus sign inside braces so KaTeX treats it as a unary sign."""
        return f"{{- {abs(n)}}}" if n < 0 else str(n)

    # original fractions as plain text (no math parsing)
    f1_txt = str(frac1).replace("\u200b", "")
    f2_txt = str(frac2).replace("\u200b", "")

    display(
        Markdown(rf"""
**Step 1:** LCM of denominators **{d1}** and **{d2}** → **{common_den}**

**Step 2:** Rewrite with common denominator  

$$
{f1_txt} = \frac{{{tex_num(n1)}}}{{{common_den}}}, \quad
{f2_txt} = \frac{{{tex_num(n2)}}}{{{common_den}}}
$$

**Step 3:** Perform the operation  

$$
{n1}\ {op_sym}\ {n2} = {result_num}
$$

**Step 4:** Simplify  

$$
\frac{{{tex_num(result_num)}}}{{{common_den}}} = {result}
$$
    """)
    )

    return result
