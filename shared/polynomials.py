"""
shared/polynomials.py — canonical polynomial and monomial helpers.

This is the single source of truth for the helper functions taught across the
polynomial notebooks (15, 17, 18, 19, and onward). Each function is *taught*
inline, as code, in exactly one notebook — that notebook's markdown explains
what it does and why. Every other notebook that needs the function imports it
from here rather than re-pasting it, so a fix only has to happen once.

Origin of each function (where it's taught inline, with the full explanation):
  - poly_str, poly_eval, poly_clean,
    poly_add, poly_negate, poly_subtract      -> notebook 15
  - mono_str, mono_eval,
    mono_multiply, mono_divide, mono_power,
    mv_str, mv_eval, mv_multiply,
    mv_divide, mv_power                        -> notebook 17
  - poly_mul_mono, poly_div_mono,
    poly_multiply, poly_divmod,
    poly_to_np, np_to_poly                     -> notebook 18
  - coeff_gcf, poly_gcf, factor_gcf            -> notebook 19

If you're reading this because you're building a new notebook: don't import
a helper you're about to teach for the first time -- write it inline there,
the way notebook 15 does with poly_str. Only import helpers the reader has
already seen taught in an earlier notebook. When you add a new one here,
add its origin to the list above.
"""

from fractions import Fraction
from math import gcd
from functools import reduce


# ============================================================
# From notebook 15 — polynomial as {exponent: coefficient} dict
# ============================================================

def poly_str(p):
    """Format a {exp: coeff} dict as a polynomial string in standard form."""
    if not p:
        return '0'
    terms = []
    for exp in sorted(p.keys(), reverse=True):
        coeff = p[exp]
        if coeff == 0:
            continue
        if exp == 0:
            terms.append(str(coeff))
        elif exp == 1:
            if coeff == 1:
                terms.append('x')
            elif coeff == -1:
                terms.append('-x')
            else:
                terms.append(f'{coeff}x')
        else:
            if coeff == 1:
                terms.append(f'x^{exp}')
            elif coeff == -1:
                terms.append(f'-x^{exp}')
            else:
                terms.append(f'{coeff}x^{exp}')
    result = ' + '.join(terms)
    return result.replace('+ -', '- ')


def poly_eval(p, x):
    """Evaluate a polynomial dict at x."""
    return sum(coeff * (x ** exp) for exp, coeff in p.items())


def poly_clean(p):
    """Remove zero-coefficient terms; convert Fraction to int where exact."""
    out = {}
    for exp, coeff in p.items():
        if isinstance(coeff, Fraction) and coeff.denominator == 1:
            coeff = int(coeff)
        if coeff != 0:
            out[exp] = coeff
    return out


def poly_add(p1, p2):
    """Add two polynomials — merge dicts by summing coefficients for matching keys."""
    result = {}
    for exp in set(p1.keys()) | set(p2.keys()):
        coeff = p1.get(exp, 0) + p2.get(exp, 0)
        if coeff != 0:
            result[exp] = coeff
    return result


def poly_negate(p):
    """Negate a polynomial — flip every coefficient. Distributing -1."""
    return {exp: -coeff for exp, coeff in p.items()}


def poly_subtract(p1, p2):
    """Subtract p2 from p1."""
    return poly_add(p1, poly_negate(p2))


# ============================================================
# From notebook 17 — single monomial as (coeff, exp), and
# multi-variable monomial as (coeff, {var: exp})
# ============================================================

def mono_str(coeff, exp, var='x'):
    """Format (coeff, exp) as a readable monomial string."""
    if exp == 0:
        return str(coeff)
    var_part = var if exp == 1 else f'{var}^{exp}'
    if coeff == 1:
        return var_part
    if coeff == -1:
        return f'-{var_part}'
    return f'{coeff}{var_part}'


def mono_eval(coeff, exp, x):
    return coeff * (x ** exp)


def mono_multiply(c1, e1, c2, e2):
    """Multiply two monomials: coefficients multiply, exponents add."""
    return c1 * c2, e1 + e2


def mono_divide(c1, e1, c2, e2):
    """Divide two monomials: coefficients divide, exponents subtract."""
    return Fraction(c1, c2), e1 - e2


def mono_power(coeff, exp, n):
    """Raise a monomial to a power: coefficient to the power, exponent multiplied."""
    return coeff ** n, exp * n


def mv_str(coeff, vars_dict):
    """Format a multi-variable monomial (coeff, {var: exp}) as a string."""
    if coeff == 0:
        return '0'
    parts = []
    if coeff == 1 and vars_dict:
        pass
    elif coeff == -1 and vars_dict:
        parts.append('-')
    else:
        parts.append(str(coeff))
    for var in sorted(vars_dict):
        exp = vars_dict[var]
        if exp == 0:
            continue
        parts.append(var if exp == 1 else f'{var}^{exp}')
    return ''.join(parts) if parts else '1'


def mv_eval(coeff, vars_dict, val_map):
    result = coeff
    for var, exp in vars_dict.items():
        result *= val_map[var] ** exp
    return result


def mv_multiply(c1, v1, c2, v2):
    """Multiply two multi-variable monomials."""
    c_res = c1 * c2
    all_vars = set(v1) | set(v2)
    v_res = {var: v1.get(var, 0) + v2.get(var, 0) for var in all_vars}
    v_res = {k: v for k, v in v_res.items() if v != 0}
    return c_res, v_res


def mv_divide(c1, v1, c2, v2):
    """Divide two multi-variable monomials."""
    c_res = Fraction(c1, c2)
    all_vars = set(v1) | set(v2)
    v_res = {var: v1.get(var, 0) - v2.get(var, 0) for var in all_vars}
    v_res = {k: v for k, v in v_res.items() if v != 0}
    return c_res, v_res


def mv_power(coeff, vars_dict, n):
    """Raise a multi-variable monomial to a power."""
    return coeff ** n, {var: exp * n for var, exp in vars_dict.items()}


# ============================================================
# From notebook 18 — multiplying and dividing full polynomials
# ============================================================

def poly_mul_mono(poly, mono_coeff, mono_exp):
    """Multiply a polynomial by a monomial."""
    return {exp + mono_exp: coeff * mono_coeff for exp, coeff in poly.items()}


def poly_div_mono(poly, mono_coeff, mono_exp):
    """Divide a polynomial by a monomial."""
    result = {}
    for exp, coeff in poly.items():
        r_exp = exp - mono_exp
        r_coeff = Fraction(coeff, mono_coeff)
        result[r_exp] = r_coeff
    return poly_clean(result)


def poly_multiply(p1, p2):
    """Multiply two polynomials — nested loop over all term pairs."""
    result = {}
    for e1, c1 in p1.items():
        for e2, c2 in p2.items():
            exp = e1 + e2
            coeff = c1 * c2
            result[exp] = result.get(exp, 0) + coeff
    return poly_clean(result)


def poly_divmod(dividend, divisor):
    """Polynomial long division. Returns (quotient, remainder) as poly dicts."""
    remainder = {k: Fraction(v) for k, v in dividend.items()}
    quotient = {}

    deg_d = max(divisor)
    lead_d = Fraction(divisor[deg_d])

    while remainder and max(remainder) >= deg_d:
        deg_r = max(remainder)
        lead_r = remainder[deg_r]

        q_coeff = lead_r / lead_d
        q_exp = deg_r - deg_d

        quotient[q_exp] = quotient.get(q_exp, Fraction(0)) + q_coeff

        for exp, coeff in divisor.items():
            new_exp = exp + q_exp
            remainder[new_exp] = remainder.get(new_exp, Fraction(0)) - q_coeff * coeff

        remainder = {k: v for k, v in remainder.items() if v != 0}

    return poly_clean(quotient), poly_clean(remainder)


def poly_to_np(p):
    """Convert {exp: coeff} dict to numpy coefficient array (highest degree first)."""
    import numpy as np
    if not p:
        return np.array([0])
    max_exp = max(p)
    arr = np.zeros(max_exp + 1)
    for exp, coeff in p.items():
        arr[max_exp - exp] = coeff
    return arr


def np_to_poly(arr):
    """Convert numpy coefficient array back to {exp: coeff} dict."""
    n = len(arr) - 1
    return {n - i: float(c) for i, c in enumerate(arr) if c != 0}


# ============================================================
# From notebook 19 — factoring out the greatest common factor
# ============================================================

def coeff_gcf(coeffs):
    """Greatest common factor of a list of integer coefficients (sign-agnostic)."""
    return reduce(gcd, (abs(c) for c in coeffs))


def poly_gcf(poly):
    """Return (gcf_coeff, gcf_exp) -- the GCF of a polynomial's terms, as a monomial."""
    coeffs = list(poly.values())
    exps = list(poly.keys())
    g_coeff = coeff_gcf(coeffs)
    g_exp = min(exps)          # the variable part every term can spare -- the SMALLEST exponent present
    leading_exp = max(exps)
    if poly[leading_exp] < 0:  # convention: factor out a negative so the remaining leading term is positive
        g_coeff = -g_coeff
    return g_coeff, g_exp


def factor_gcf(poly):
    """Factor a polynomial as gcf * remaining. Returns (gcf_coeff, gcf_exp, remaining_poly)."""
    g_coeff, g_exp = poly_gcf(poly)
    remaining = poly_div_mono(poly, g_coeff, g_exp)
    return g_coeff, g_exp, remaining
