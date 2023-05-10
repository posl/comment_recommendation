def g_1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    return int("".join(x))

if __name__ == '__main__':
    g_1()