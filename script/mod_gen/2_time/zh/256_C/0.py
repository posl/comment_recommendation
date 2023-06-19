def f(h, w):
    if h == 0 and w == 0:
        return 1
    elif h <= 0 or w <= 0:
        return 0
    elif dp[h][w] != -1:
        return dp[h][w]
    else:
        dp[h][w] = f(h-1, w) + f(h-1, w-1) + f(h-1, w-2) + f(h-2, w) + f(h-2, w-1) + f(h-3, w)
        return dp[h][w]
h1, h2, h3, w1, w2, w3 = map(int, input().split())
dp = [[-1 for _ in range(31)] for _ in range(31)]
print(f(h1, w1) * f(h2, w2) * f(h3, w3))
