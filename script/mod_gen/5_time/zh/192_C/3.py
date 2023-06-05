def g_1(x):
    s = str(x)
    l = list(s)
    l.sort(reverse=True)
    s = ''.join(l)
    return int(s)

if __name__ == '__main__':
    g_1()