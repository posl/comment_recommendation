def main():
    H, W, A, B = map(int, input().split())
    MOD = 10 ** 9 + 7
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD
            if i + 1 < H and j + 1 < W and i + 1 - A >= 0 and j + 1 - B >= 0:
                dp[i + 1][j + 1] += dp[i + 1 - A][j + 1 - B]
                dp[i + 1][j + 1] %= MOD
    print(dp[H][W])
