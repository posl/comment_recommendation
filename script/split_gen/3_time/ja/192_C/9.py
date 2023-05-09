def g1(x):
    s = str(x)
    return int(''.join(sorted(s, reverse=True)))
