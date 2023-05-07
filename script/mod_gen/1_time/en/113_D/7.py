def main():
    H, W, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    dp = [[0] * (W + 2) for i in range(H + 1)]
    dp[0][1] = 1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 1:
                dp[i][j] += dp[i - 1][j - 1]
            if j < W:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD
    print(dp[H][K])

if __name__ == '__main__':
    main()