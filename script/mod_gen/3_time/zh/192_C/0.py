def g_1(x):
    y = str(x)
    y = list(y)
    y.sort(reverse=True)
    y = ''.join(y)
    y = int(y)
    return y

if __name__ == '__main__':
    g_1()