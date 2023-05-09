def calc(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x
    else:
        return x + y + calc(n-1, x, y)
