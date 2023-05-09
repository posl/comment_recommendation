def solve(n, m, k):
    mod = 998244353
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k + 1):
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod
            if j + m < k + 1:
                dp[i + 1][j + m] = (dp[i + 1][j + m] + dp[i][j]) % mod
            else:
                dp[i + 1][k] = (dp[i + 1][k] + dp[i][j]) % mod
    return dp[n][k]

if __name__ == '__main__':
    solve()