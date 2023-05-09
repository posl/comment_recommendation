def problem227_a():
    n, k, a = map(int, input().split())
    print((k - a) % (n - a) + a)
