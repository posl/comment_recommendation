def amidakuji(H, W, K):
    if W == 1:
        return 1
    dp = [[0 for _ in range(W)] for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(1, H + 1):
        for j in range(W):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == W - 1:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            dp[i][j] %= 1000000007
    return dp[H][K - 1]

if __name__ == '__main__':
    amidakuji()