def func(a, b):
    if a == b:
        return a
    else:
        return func(a, b-1) | b
