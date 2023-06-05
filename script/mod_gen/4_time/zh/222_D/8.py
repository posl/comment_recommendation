def solve(n, a, b):
    mod = 998244353
    dp = [[0 for i in range(3001)] for j in range(n)]
    for i in range(a[0], b[0] + 1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(3001):
            dp[i][j] = dp[i - 1][j]
        for j in range(a[i], b[i] + 1):
            dp[i][j] += dp[i][j - 1]
            dp[i][j] %= mod
    return dp[n - 1][b[n - 1]]

if __name__ == '__main__':
    solve()