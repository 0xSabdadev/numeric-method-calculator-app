import re
import sympy as sym
import pandas as pd
from math import *

#========================================================================

def f(x, p):
    return (eval(p))

def derivative(p):
    x = sym.Symbol("x")
    return sym.diff(p)

def integral(p):
    x = sym.Symbol("x")
    return sym.integrate(p)

#========================================================================

def build_expr(substr):
    pattern = r"[0-9]x"
    if (substr.find("^")):
        substr = substr.replace("^", "**")
    if re.search(pattern, substr):
        substr = substr.replace("x", "*x")
    return substr

def change_expr(str):
    expr = str.split(" ")
    expr = [build_expr(item) for item in expr]
    expr = " ".join(expr)
    return expr

#========================================================================

def rebuild_expr(substr):
    if (substr.find("**")):
        substr = substr.replace("**", "^")
    if (substr.find("*")):
        substr = substr.replace("*", "")
    return substr

def rechange_expr(str):
    expr = str.split(" ")
    expr = [rebuild_expr(item) for item in expr]
    expr = " ".join(expr)
    return expr

#========================================================================

def to_df(body, head):
    pd.options.display.float_format = '{:.6f}'.format
    return pd.DataFrame(body, columns=head)