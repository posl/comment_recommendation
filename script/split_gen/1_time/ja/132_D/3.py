def nCk(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= (n - i)
        b *= (i + 1)
    return a // b
