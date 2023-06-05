def calc_cost(n, a, x, y):
    if n <= a:
        return n * x
    else:
        return a * x + (n - a) * y
