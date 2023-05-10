def solve(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] == -1:
            continue
        for j in range(m):
            dp[i + a[j]] = max(dp[i + a[j]], dp[i] * 10 + a[j])
    return dp[n]
