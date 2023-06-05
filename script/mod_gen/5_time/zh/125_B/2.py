def get_max_value(n, v, c):
    dp = [[0 for _ in range(10000)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(10000):
            if j < c[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - c[i]] + v[i])
    return dp[n][9999]

if __name__ == '__main__':
    get_max_value()