def f(n, a, b):
    if n <= a:
        return n
    else:
        return a + (n - a) * b
