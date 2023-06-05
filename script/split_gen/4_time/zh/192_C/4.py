def g_1(x):
    x_str = str(x)
    x_str = sorted(x_str,reverse=True)
    x_str = ''.join(x_str)
    x_int = int(x_str)
    return x_int
