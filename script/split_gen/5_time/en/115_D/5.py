def burger(n,x):
    if n == 0:
        return 0
    elif x == 1:
        return 0
    elif x <= 1 + (2 ** (n + 1) - 3):
        return burger(n - 1, x - 1)
    elif x == 2 + (2 ** (n + 1) - 3):
        return 1 + (2 ** n - 1)
    elif x <= 2 * (2 ** (n + 1) - 3):
        return 1 + (2 ** n - 1) + burger(n - 1, x - 2 - (2 ** (n + 1) - 3))
    else:
        return 2 * (2 ** n - 1)
