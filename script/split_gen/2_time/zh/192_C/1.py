def g_1(x):
    a = list(str(x))
    a.sort(reverse=True)
    return int(''.join(a))
