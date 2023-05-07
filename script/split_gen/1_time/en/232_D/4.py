def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if C[h][w] == "#":
                continue
            if h > 0:
                dp[h][w] += dp[h - 1][w]
            if w > 0:
                dp[h][w] += dp[h][w - 1]
    print(dp[-1][-1] % (10 ** 9 + 7))
