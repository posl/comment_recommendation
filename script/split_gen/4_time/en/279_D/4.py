def solve():
    a, b = map(int, input().split())
    g = 1
    res = a
    while g < a / 2:
        t = g + a / (2 * g)
        if t < res:
            res = t
        g += b
    print(res)
