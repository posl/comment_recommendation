def func(n, a, b):
    res = 0
    for i in range(n):
        res += (b[i] - a[i] + 1) * (a[i] + b[i]) / 2
    return res
