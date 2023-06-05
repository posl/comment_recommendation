def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    y = (2 ** (n + 2)) - 3
    if x <= 1:
        return 0
    elif x <= y:
        return f(n - 1, x - 1)
    elif x == y + 1:
        return 1 + (2 ** n - 1)
    elif x <= 2 * y + 2:
        return 1 + (2 ** n - 1) + f(n - 1, x - y - 2)
    else:
        return 2 * (2 ** n - 1)
