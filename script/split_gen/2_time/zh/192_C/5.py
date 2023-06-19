def g1(x):
    x = str(x)
    x = ''.join(sorted(x, reverse=True))
    return int(x)
