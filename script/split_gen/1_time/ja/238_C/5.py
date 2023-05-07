def f(x):
    if x < 10:
        return x
    else:
        return 9 + (x-9) * len(str(x))
