def f(m, a):
    res = 0
    for i in range(len(a)):
        res += m % a[i]
    return res
