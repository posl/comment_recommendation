def main():
    N, K = [int(x) for x in input().split()]
    MOD = 10**9 + 7
    # dp[i][j] = number of ways to arrange j balls so that Takahashi will need exactly i moves to collect all the blue balls
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    # dp[0][j] = 1
    for j in range(N + 1):
        dp[0][j] = 1
    # dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + dp[i-1][j-2] + ... + dp[i-1][0]
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD
    for i in range(1, K + 1):
        print(dp[i][N])

if __name__ == '__main__':
    main()