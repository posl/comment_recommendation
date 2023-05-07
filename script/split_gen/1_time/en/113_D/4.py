def main():
    H, W, K = map(int, input().split())
    dp = [[0] * (W + 1) for i in range(H + 1)]
    dp[0][1] = 1
    MOD = 10 ** 9 + 7
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if j == 1:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
            elif j == W:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
            dp[i][j] %= MOD
    print(dp[H][K])
