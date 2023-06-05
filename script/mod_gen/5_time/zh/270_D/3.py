def get_max_stone(n, k, a):
    if n == 0:
        return 0
    # dp[i][j]表示从i移除j个棋子的最大值
    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if j >= a[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + a[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[k][n]

if __name__ == '__main__':
    get_max_stone()