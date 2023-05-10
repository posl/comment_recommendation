def f(x):
    if x <= 1:
        return 1
    return x * f(x-1)
