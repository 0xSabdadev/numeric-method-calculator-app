from .helper import *

#========================================================================

def average_error(data, category):
    total = 0
    for i in range(len(data)):
        if category == "tengah":
            total += data[i][8]
        else:
            total += data[i][7]
    return total / len(data)

#========================================================================

def metode_selisih_mundur(value):
    expr = change_expr(value["persamaan"])
    expr_ = str(derivative(expr))
    value["turunan"] = rechange_expr(expr_)
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    h = float(value["ukuran_langkah"])
    tag, result = ["i", "x", "x-h", "f(x)", "f(x-h)", "f'(x) mundur", "f'(x) eksak", "e"], []

    i = 0

    x = a

    while (x <= b):
        fx = f(x, expr)

        x_min_h = x - h
        fx_min_h = f(x_min_h, expr)

        fx_mundur = (fx - fx_min_h) / h
        fx_eksak = f(x, expr_)

        error = abs(fx_eksak - fx_mundur)

        result.append([i, x, x_min_h, fx, fx_min_h, fx_mundur, fx_eksak, error])

        i+=1

        x+=h

    tables = to_df(result, tag)
    conclusion = "Didapatkan rata-rata error = {:.6f}".format(average_error(result, "mundur"))
    return [value, tables, conclusion]

#========================================================================

def metode_selisih_tengah(value):
    expr = change_expr(value["persamaan"])
    expr_ = str(derivative(expr))
    value["turunan"] = rechange_expr(expr_)
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    h = float(value["ukuran_langkah"])
    tag, result = ["i", "x", "x+h", "x-h", "f(x+h)", "f(x-h)", "f'(x) tengah", "f'(x) eksak", "e"], []

    i = 0

    x = a

    while (x <= b):
        x_plus_h = x + h
        fx_plus_h = f(x_plus_h, expr)

        x_min_h = x - h
        fx_min_h = f(x_min_h, expr)

        fx_tengah = (fx_plus_h - fx_min_h) / (2 * h)
        fx_eksak = f(x, expr_)

        error = abs(fx_eksak - fx_tengah)

        result.append([i, x, x_plus_h, x_min_h, fx_plus_h, fx_min_h, fx_tengah, fx_eksak, error])

        i+=1

        x+=h

    tables = to_df(result, tag)
    conclusion = "Didapatkan rata-rata error = {:.6f}".format(average_error(result, "tengah"))
    return [value, tables, conclusion]

#========================================================================

def metode_selisih_maju(value):
    expr = change_expr(value["persamaan"])
    expr_ = str(derivative(expr))
    value["turunan"] = rechange_expr(expr_)
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    h = float(value["ukuran_langkah"])
    tag, result = ["i", "x", "x+h", "f(x)", "f(x+h)", "f'(x) maju", "f'(x) eksak", "e"], []

    i = 0

    x = a

    while (x <= b):
        fx = f(x, expr)

        x_plus_h = x + h
        fx_plus_h = f(x_plus_h, expr)

        fx_maju = (fx_plus_h - fx) / h
        fx_eksak = f(x, expr_)

        error = abs(fx_eksak - fx_maju)

        result.append([i, x, x_plus_h, fx, fx_plus_h, fx_maju, fx_eksak, error])

        i+=1

        x+=h

    tables = to_df(result, tag)
    conclusion = "Didapatkan rata-rata error = {:.6f}".format(average_error(result, "maju"))
    return [value, tables, conclusion]