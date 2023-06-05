def f(n):
    if n >= 0:
        return int(n ** (1 / 3))
    else:
        return -int((-n) ** (1 / 3))
