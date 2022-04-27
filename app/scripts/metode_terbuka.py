from .helper import *

#========================================================================

def message(n, e, root):
    return """Karena pada iterasi ke-{} nilai error lebih kecil dari {}, 
    maka iterasi dihentikan dan diperoleh solusi persamaan non linier 
    yang diinginkan yaitu aproksimasi akar = {:.6f}""".format(n, e, root)

#========================================================================

def metode_newton_raphson(value):
    expr = change_expr(value["persamaan"])
    expr_ = str(derivative(expr))
    value["turunan"] = rechange_expr(expr_)
    x1 = float(value["tebakan_awal"])
    tolerance = float(value["toleransi_error"])
    tag, result = ["i", "x1", "x2", "f(x1)", "f(x2)", "e"], []

    i = 1

    while True:
        fx1, f_x1 = f(x1, expr), f(x1, expr_)
        x2 = x1 - (fx1 / f_x1)
        fx2 = f(x2, expr)
        e = abs(fx2)

        result.append([i, x1, x2, fx1, fx2, e])

        if (e < tolerance):
            tables = to_df(result, tag)
            conclusion = message(i, tolerance, x2)
            return [value, tables, conclusion]
            
        x1 = x2

        i += 1

#========================================================================

def metode_secant(value):
    expr = change_expr(value["persamaan"])
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    tolerance = float(value["toleransi_error"])
    tag, result = ["i", "a", "b", "c", "f(a)", "f(b)", "f(c)", "e"], []

    i = 1

    while True:
        fa, fb = f(a, expr), f(b, expr)
        c = b - (fb*(b - a) / (fb - fa))
        fc = f(c, expr)
        e = abs((c - b) / c)

        result.append([i, a, b, c, fa, fb, fc, e])

        if (e < tolerance):
            tables = to_df(result, tag)
            conclusion = message(i, tolerance, c)
            return [value, tables, conclusion]

        a, b = b, c

        i += 1

#========================================================================

def metode_iterasi_sederhana(value):
    expr = change_expr(value["persamaan"])
    expr_gx = value["persamaan_gx"]
    x = float(value["tebakan_awal"])
    tolerance = float(value["toleransi_error"])
    tag, result = ["i", "Xr", "|Xr+1 - Xr|"], []

    i = 0

    while True:
        if i == 0:
            x = x
            e = None
        else:
            x = f(result[i-1][1], expr_gx)
            e = abs(x - result[i-1][1])
        
        result.append([i+1, x, e])

        if i > 0:
            if e < tolerance:
                tables = to_df(result, tag)
                conclusion = message(i, tolerance, result[i][1])
                return [value, tables, conclusion]

        i += 1