def solve(n, m, q, w, v, x, query):
    # dp[i][j][k]表示前i件物品中，放入j个箱子，且第j个箱子放入第k件物品的最大价值
    dp = [[[0 for k in range(n + 1)] for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, n + 1):
                if k == i and x[j - 1] >= w[i - 1]:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1] + v[i - 1])
                else:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])
    res = []
    for i in range(q):
        l, r = query[i]
        tmp = 0
        for j in range(1, n + 1):
            tmp = max(tmp, dp[j][r][j])
        res.append(tmp)
    return res
