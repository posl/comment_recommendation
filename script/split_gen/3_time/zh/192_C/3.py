def g_1(x):
    a = []
    while x != 0:
        a.append(x % 10)
        x = x // 10
    a.sort(reverse=True)
    b = ''.join(str(i) for i in a)
    return int(b)
