def f(x, a):
    s = 0
    for i in range(len(a)):
        s += x ^ a[i]
    return s
