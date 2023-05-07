def solve(n, m, a, b):
    a = [0] + a
    b = [0] + b
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j - a[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - a[i]] + b[i])
    return dp[n][m]

if __name__ == '__main__':
    solve()