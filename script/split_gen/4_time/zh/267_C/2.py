def max_sum(n, m, a):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i - 1] + a[i - 1]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i >= m:
            dp[i] = max(dp[i - 1], res[i] - res[i - m])
    return dp[n]
