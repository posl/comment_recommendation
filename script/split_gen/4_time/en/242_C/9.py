def find_combinations(n):
    dp = [[0 for i in range(10)] for j in range(n)]
    for i in range(10):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % 998244353
            elif j == 9:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 998244353
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]) % 998244353
    return sum(dp[n - 1]) % 998244353
