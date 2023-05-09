def calc(n, p, q):
    a = 0
    b = 0
    for i in range(n):
        a = a + (p[i] - 1) * factorial(n - i - 1, p)
        b = b + (q[i] - 1) * factorial(n - i - 1, q)
        #print(a, b, p[i], q[i])
    return abs(a - b)
