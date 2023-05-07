def f(x):
    s = str(x)
    s = ''.join(sorted(s))
    g1 = int(s[::-1])
    g2 = int(s)
    return g1 - g2
