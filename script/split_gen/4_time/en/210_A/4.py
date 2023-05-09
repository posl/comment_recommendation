def problem210_a():
    n, a, x, y = map(int, input().split())
    print(min(n, a) * x + max(0, n - a) * y)
