def f(n):
    if n < 1000:
        return 0
    else:
        return 1 + f(n/1000)
