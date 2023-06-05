def f(h, w):
    if h == 0 and w == 0:
        return 1
    if h < 0 or w < 0:
        return 0
    if memo[h][w] != -1:
        return memo[h][w]
    memo[h][w] = f(h - 1, w) + f(h - 2, w) + f(h - 3, w) + f(h, w - 1) + f(h, w - 2) + f(h, w - 3)
    return memo[h][w]
memo = [[-1 for _ in range(31)] for _ in range(31)]
h1, h2, h3, w1, w2, w3 = map(int, input().split())
print(f(h1, w1) * f(h2, w2) * f(h3, w3))
