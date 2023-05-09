def g1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = int(''.join(x))
    return x
