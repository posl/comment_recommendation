def input():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        t, d = map(int, input().split())
        sushi.append((d, t))
    return n, k, sushi
