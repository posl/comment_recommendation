def problem227_a():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        print(k%n)
