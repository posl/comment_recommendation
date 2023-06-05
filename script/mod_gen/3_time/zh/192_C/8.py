def g_1(x):
    x = str(x)
    x = sorted(x, reverse=True)
    x = ''.join(x)
    x = int(x)
    return x

if __name__ == '__main__':
    g_1()