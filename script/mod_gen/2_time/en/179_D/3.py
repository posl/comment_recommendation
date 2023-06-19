def solve(n, k, lrs):
    mod = 998244353
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n):
        for l, r in lrs:
            dp[i + l] += dp[i]
            dp[i + l] %= mod
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= mod
    return dp[n]
n, k = map(int, input().split())
lrs = [map(int, input().split()) for _ in range(k)]
print(solve(n, k, lrs))
