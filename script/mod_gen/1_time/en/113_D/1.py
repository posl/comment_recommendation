def main():
    H, W, K = map(int, input().split())
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][1] = 1
    mod = 10 ** 9 + 7
    for i in range(H):
        for j in range(1, W + 1):
            if j == 1:
                dp[i + 1][j] = dp[i + 1][j] + dp[i][j] + dp[i][j + 1]
            elif j == W:
                dp[i + 1][j] = dp[i + 1][j] + dp[i][j] + dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i + 1][j] + dp[i][j] + dp[i][j - 1] + dp[i][j + 1]
            dp[i + 1][j] %= mod
    print(dp[H][K])

if __name__ == '__main__':
    main()