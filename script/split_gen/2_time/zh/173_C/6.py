def solve(H, W, K, c):
    # dp[h][w][k] = (h行w列，剩余k个黑色的方块)的方案数
    dp = [[[0 for k in range(K+1)] for w in range(W+1)] for h in range(H+1)]
    dp[0][0][0] = 1
    for h in range(H):
        for w in range(W):
            for k in range(K+1):
                # 不选
                dp[h+1][w][k] += dp[h][w][k]
                dp[h][w+1][k] += dp[h][w][k]
                # 选
                if c[h][w] == "#":
                    if k+1 <= K:
                        dp[h+1][w][k+1] += dp[h][w][k]
                        dp[h][w+1][k+1] += dp[h][w][k]
    return dp[H][W][K]
H, W, K = map(int, input().split())
c = [input() for _ in range(H)]
print(solve(H, W, K, c))
