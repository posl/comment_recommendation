def g_1(x):
    s = str(x)
    s = sorted(s,reverse=True)
    return int(''.join(s))
