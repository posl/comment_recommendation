def solve(n, c, a, b, cost):
    dp = [0] * (10**9 + 1)
    for i in range(n):
        dp[a[i]] += cost[i]
        dp[b[i] + 1] -= cost[i]
    for i in range(10**9):
        dp[i + 1] += dp[i]
    return min(c, min(dp))
