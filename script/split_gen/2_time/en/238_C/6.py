def f(x):
    if x <= 0:
        return 0
    if x < 10:
        return x
    n = len(str(x))
    return 9 * 10 ** (n - 2) + n * f(x % 10 ** (n - 1)) + f(x // 10)
