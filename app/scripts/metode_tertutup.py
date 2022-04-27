from .helper import *

#========================================================================

def existence_of_roots(x, y, expression):
    if f(x, expression) * f(y, expression) < 0:
        return True
    else:
        return False

#========================================================================

def failure_message(x, y):
    return """Pada metode tertutup jika f(a).f(b) > 0, 
    maka tidak terdapat akar persamaan pada selang 
    [{}, {}].""".format(x, y)

#========================================================================

def message_one(a, b, fa, fb, root):
    return """Diperoleh penyelesaian di antara {} dan {} dengan 
    nilai f(x) masing-masing {:.6f} dan {:.6f}, sehingga dapat 
    diambil penyelesaian x = {}""".format(a, b, fa, fb, root)

#========================================================================

def message_two(n, e, root):
    return """Karena pada iterasi ke-{} nilai error lebih kecil dari {}, 
    maka iterasi dihentikan dan diperoleh solusi persamaan non linier 
    yang diinginkan yaitu aproksimasi akar = {:.6f}""".format(n, e, root)

#========================================================================

def metode_tabel(value):
    expr = change_expr(value["persamaan"])
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    n = int(value["jumlah_pembagi"])
    tag, result = ["x", "f(x)"], []

    h = (b - a) / n; value["ukuran_langkah"] = h

    if existence_of_roots(a, b, expr):
        for i in range(n+1):
            x = a + (i * h)
            fx = f(x, expr)
            result.append([x, fx])

        for i in range(n+1):
            x, fx = result[i][0], result[i][1]
            xi, fxi = result[i+1][0], result[i+1][1]

            if fx == 0:
                tables = to_df(result, tag)
                conclusion = message_one(x, xi, fx, fxi, x)
                return [value, tables, conclusion]

            if fx * fxi < 0:
                if abs(fx) <= abs(fxi):
                    tables = to_df(result, tag)
                    conclusion = message_one(x, xi, fx, fxi, x)
                    return [value, tables, conclusion]
                else:
                    tables = to_df(result, tag)
                    conclusion = message_one(x, xi, fx, fxi, x)
                    return [value, tables, conclusion]
    else:
        return [value, failure_message(a, b)]

#========================================================================

def metode_biseksi(value):
    expr = change_expr(value["persamaan"])
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    tolerance = float(value["toleransi_error"])
    tag, result = ["i", "a", "c", "b", "f(a)", "f(c)", "f(b)", "e"], []

    i = 1

    if existence_of_roots(a, b, expr):
        while True:
            fa, fb = f(a, expr), f(b, expr)
            c = (a + b) / 2
            fc = f(c, expr)
            e = abs(fc)

            result.append([i, a, c, b, fa, fc, fb, e])

            if (e < tolerance):
                tables = to_df(result, tag)
                conclusion = message_two(i, tolerance, c)
                return [value, tables, conclusion]

            if (fa*fc) < 0:
                b = c
            else:
                a = c

            i += 1
    else:
        return [value, failure_message(a, b)]

#========================================================================

def metode_regula_falsi(value):
    expr = change_expr(value["persamaan"])
    a, b = float(value["batas_bawah"]), float(value["batas_atas"])
    tolerance = float(value["toleransi_error"])
    tag, result = ["i", "a", "c", "b", "f(a)", "f(c)", "f(b)", "e"], []

    i = 1

    if existence_of_roots(a, b, expr):
        while True:
            fa, fb = f(a, expr), f(b, expr)
            c = (b - (fb*(b - a) / (fb - fa)))
            fc = f(c, expr)
            e = abs(fc)

            result.append([i, a, c, b, fa, fc, fb, e])

            if (e < tolerance):
                tables = to_df(result, tag)
                conclusion = message_two(i, tolerance, c)
                return [value, tables, conclusion]

            if (fa*fc) < 0:
                b = c
            else:
                a = c

            i += 1
    else:
        return [value, failure_message(a, b)]