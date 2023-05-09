def f(n):
    if n == 0:
        return 0
    if n < 10:
        return n
    k = len(str(n))
    return (n - 10 ** (k - 1) + 1) + 9 * (k - 1) * (10 ** (k - 2))
