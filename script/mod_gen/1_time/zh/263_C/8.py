def f(n, m):
    if n == 1:
        for i in range(1, m + 1):
            print(i)
    else:
        for i in range(m, n - 1, -1):
            f(n - 1, i - 1)
            print(i)
f(3, 5)
