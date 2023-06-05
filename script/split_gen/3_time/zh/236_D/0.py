def get_max_xor(n, a):
    dp = [[0 for i in range(1 << n)] for j in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(1 << n):
            for k in range(1 << n):
                if (j >> i & 1) == 0 and (k >> i & 1) == 0:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] + dp[i + 1][k] + a[i][k])
    return dp[0][0]
