def f(x):
    if x < 10:
        return x
    else:
        return 1 + f(x // 10)
