from .helper import *

#========================================================================

def message(l, l_eksak, e):
    return """Diperoleh luas daerah = {:.6f}, luas eksak = {:.6f},
    dan error = {:.6f}""".format(l, l_eksak, e)

#========================================================================

def metode_riemann(value):
    expr = change_expr(value["persamaan"])
    expr_ = str(integral(expr))
    value["integral"] = rechange_expr(expr_)
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    n = float(value["jumlah_pembagi"])
    tag, result = ["x", "f(x)"], []

    h = (b - a) / n; value["ukuran_langkah"] = h

    x = a

    while (x <= b):
        fx = f(x, expr)
        result.append([x, fx])
        x += h

    total = 0
    for i in range(len(result)):
        total += result[i][1]

    area = total * h
    fx_eksak = f(b, expr_) - f(a, expr_)
    error = fx_eksak - area
    
    tables = to_df(result, tag)
    conclusion = message(area, fx_eksak, error)
    return [value, tables, conclusion]

#========================================================================

def metode_trapezoida(value):
    expr = change_expr(value["persamaan"])
    expr_ = str(integral(expr))
    value["integral"] = rechange_expr(expr_)
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    n = float(value["jumlah_pembagi"])
    tag, result = ["x", "f(x)"], []

    h = (b - a) / n; value["ukuran_langkah"] = h

    x = a

    while (x <= b):
        fx = f(x, expr)
        result.append([x, fx])
        x += h

    total = 0
    for i in range(1, (len(result) - 1)):
        total += result[i][1]

    area = (h * (result[0][1] + (2 * total) + result[-1][1])) / 2
    fx_eksak = f(b, expr_) - f(a, expr_)
    error = fx_eksak - area
    
    tables = to_df(result, tag)
    conclusion = message(area, fx_eksak, error)
    return [value, tables, conclusion]

#========================================================================

def metode_simpson_v1(value):
    expr = change_expr(value["persamaan"])
    expr_ = str(integral(expr))
    value["integral"] = rechange_expr(expr_)
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    n = float(value["jumlah_pembagi"])
    tag, result = ["x", "f(x)"], []

    h = (b - a) / n; value["ukuran_langkah"] = h

    x = a

    while (x <= b):
        fx = f(x, expr)
        result.append([x, fx])
        x += h

    ganjil, genap = 0, 0
    for i in range(1, (len(result) - 1)):
        if (i % 2 == 0):
            genap += result[i][1]
        else:
            ganjil += result[i][1]

    area = (h * (result[0][1] + (4 * ganjil) + (2 * genap) + result[-1][1])) / 3
    fx_eksak = f(b, expr_) - f(a, expr_)
    error = fx_eksak - area
    
    tables = to_df(result, tag)
    conclusion = message(area, fx_eksak, error)
    return [value, tables, conclusion]


#========================================================================

def metode_simpson_v2(value):
    expr = change_expr(value["persamaan"])
    expr_ = str(integral(expr))
    value["integral"] = rechange_expr(expr_)
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    n = float(value["jumlah_pembagi"])
    tag, result = ["x", "f(x)"], []

    h = (b - a) / n; value["ukuran_langkah"] = h

    x = a

    while (x <= b):
        fx = f(x, expr)
        result.append([x, fx])
        x += h

    kelipatan, bukan = 0, 0
    for i in range(1, (len(result) - 1)):
        if (i % 3 == 0):
            kelipatan += result[i][1]
        else:
            bukan += result[i][1]

    area = (3 * h * (result[0][1] + (3 * bukan) + (2 * kelipatan) + result[-1][1])) / 8
    fx_eksak = f(b, expr_) - f(a, expr_)
    error = fx_eksak - area
    
    tables = to_df(result, tag)
    conclusion = message(area, fx_eksak, error)
    return [value, tables, conclusion]