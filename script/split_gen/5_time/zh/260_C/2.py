def f(n, x, y):
    if n == 1:
        return 1
    if n == 2:
        return 0
    return f(n-1, x, y) + f(n-2, x, y) + x * f(n-1, x, y) + y * f(n-2, x, y)
