def calc(n, x, y):
    if n == 1:
        return 1
    if n == 2:
        return x + y
    return calc(n-1, x, y) + calc(n-2, x, y)
