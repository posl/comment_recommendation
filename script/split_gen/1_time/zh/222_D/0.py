def func(n, a, b):
    result = 1
    for i in range(n):
        result *= (b[i] - a[i] + 1)
    return result % 998244353
