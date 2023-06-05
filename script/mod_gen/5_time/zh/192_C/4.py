def g_1(x):
    x = list(str(x))
    x.sort(reverse=True)
    x = int(''.join(x))
    return x

if __name__ == '__main__':
    g_1()