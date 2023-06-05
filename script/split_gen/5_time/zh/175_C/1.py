def problems175_c():
    x, k, d = map(int, input().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
        return
    if (k - x // d) % 2 == 0:
        print(x % d)
        return
    print(d - x % d)
