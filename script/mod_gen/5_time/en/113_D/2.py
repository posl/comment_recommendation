def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][1] = 1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j - 1] * dp[i - 1][j] + dp[i - 1][j] * dp[i - 1][j + 1] + dp[i - 1][j] * dp[i - 1][j] * (j - 1)
            dp[i][j] %= MOD
    print(dp[H][K])
main()
