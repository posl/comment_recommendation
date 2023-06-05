def f(m, a):
    s = 0
    for i in range(len(a)):
        s += m % a[i]
    return s
