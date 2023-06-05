def f(x, n, s, w):
    c = 0
    for i in range(n):
        if s[i] == '0':
            if x > w[i]:
                c += 1
        else:
            if x <= w[i]:
                c += 1
    return c
