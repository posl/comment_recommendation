def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j > 0:
                dp[i + 1][j - 1] += dp[i][j]
            if j < W - 1:
                dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j] += dp[i][j]
    print(dp[H][K - 1] % 1000000007)

if __name__ == '__main__':
    main()