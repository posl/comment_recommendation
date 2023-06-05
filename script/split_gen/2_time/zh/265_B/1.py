def problem265_a():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(int(y * n / 3))
    elif n % 3 == 1:
        print(int(y * (n - 1) / 3 + x))
    else:
        print(int(y * (n - 2) / 3 + 2 * x))
problem265_a()
