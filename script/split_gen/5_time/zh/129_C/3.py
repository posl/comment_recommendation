def climb_stairs(n, m, a):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(m):
        dp[a[i]] = -1
    for i in range(2, n + 1):
        if dp[i] != -1:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n]
