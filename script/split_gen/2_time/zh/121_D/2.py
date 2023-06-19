def f(a, b):
    if a == 0:
        return g(b)
    else:
        return g(b) ^ g(a-1)
