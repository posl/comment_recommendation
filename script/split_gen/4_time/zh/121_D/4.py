def f(a, b):
    if a == b:
        return a
    return f(a, b - 1) ^ b
