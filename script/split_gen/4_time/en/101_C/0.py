def problems101_c():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if (n - 1) % (k - 1) == 0:
        print((n - 1) // (k - 1))
    else:
        print((n - 1) // (k - 1) + 1)
