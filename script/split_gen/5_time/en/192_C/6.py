def g_1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    return int("".join(x))
