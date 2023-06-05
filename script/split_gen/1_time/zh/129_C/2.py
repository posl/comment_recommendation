def climb(n, m, a):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if i in a:
            continue
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1000000007
