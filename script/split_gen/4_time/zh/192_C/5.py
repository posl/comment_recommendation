def g_1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = int(''.join(x))
    return x
