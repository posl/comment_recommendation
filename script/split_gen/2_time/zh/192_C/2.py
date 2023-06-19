def g1(x):
    x = str(x)
    x = list(x)
    x.sort()
    x = ''.join(x)
    return int(x)
