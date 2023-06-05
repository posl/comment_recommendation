def solve(n, m, a, b):
    # 从第i项工作开始，可以获得的最大总奖励
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        # 从第i项工作开始，可以获得的最大总奖励
        dp[i] = max(dp[i + 1], dp[i + a[i]] + b[i])
    return dp[0]
