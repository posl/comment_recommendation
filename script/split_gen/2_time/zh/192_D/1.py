def g1(x):
    s = str(x)
    s = sorted(s, reverse=True)
    s = ''.join(s)
    return int(s)
