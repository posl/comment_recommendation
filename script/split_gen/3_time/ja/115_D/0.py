def burger(n, x):
    if n == 0:
        return 1 if x > 0 else 0
    if x <= 1 + 2 ** (n - 1):
        return burger(n - 1, x - 1)
    return burger(n - 1, x - 1) + 1 + burger(n - 1, x - 2 - 2 ** (n - 1))
