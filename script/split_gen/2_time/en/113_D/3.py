def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (W + 2) for _ in range(H + 1)]
    dp[0][1] = 1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j] * (W - 2) + dp[i - 1][j - 1] * (j - 2) + dp[i - 1][j + 1] * (W - j - 1)
            dp[i][j] %= MOD
    print(dp[H][K])
