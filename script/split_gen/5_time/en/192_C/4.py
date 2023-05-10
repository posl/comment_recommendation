def g_1(x):
    x = list(str(x))
    x.sort(reverse=True)
    return int(''.join(x))
