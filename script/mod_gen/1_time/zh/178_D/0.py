def solve(n):
    mod = 10**9 + 7
    dp = [[0 for i in range(n+1)] for i in range(n+1)]
    dp[0][0] = 1
    for i in range(3, n+1):
        for j in range(n+1):
            if j - i >= 0:
                dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % mod
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][n]

if __name__ == '__main__':
    solve()