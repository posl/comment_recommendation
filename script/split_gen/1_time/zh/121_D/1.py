def f(a, b):
    if a == b:
        return a
    else:
        return b | f(a, b-1)
