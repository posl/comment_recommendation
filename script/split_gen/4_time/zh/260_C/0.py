def func(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    else:
        return func(n-1, x, y) + func(n-2, x, y) + y
