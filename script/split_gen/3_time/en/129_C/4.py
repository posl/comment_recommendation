def solve(n, m, a):
    MOD = 10**9 + 7
    dp = [0] * (n+1)
    dp[0] = 1
    broken = set(a)
    for i in range(1, n+1):
        if i in broken:
            continue
        if i == 1:
            dp[i] = dp[i-1]
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
    return dp[n]
