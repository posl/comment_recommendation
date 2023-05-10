def g_1(x):
    x = list(str(x))
    x.sort(reverse=True)
    return int(''.join(x))

if __name__ == '__main__':
    g_1()