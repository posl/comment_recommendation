def f(a, b):
    if a == b:
        return a
    else:
        return (a & b) + f(a+1, b)
