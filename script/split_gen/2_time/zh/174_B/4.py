def f1(n,d,x,y):
    n = int(n)
    d = int(d)
    x = int(x)
    y = int(y)
    r = 0
    for i in range(n):
        if (x[i]**2 + y[i]**2)**0.5 <= d:
            r += 1
    return r
