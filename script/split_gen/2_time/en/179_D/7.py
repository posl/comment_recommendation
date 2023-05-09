def solve():
    n, k = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(k)]
    mod = 998244353
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        for lr in lrs:
            l, r = lr
            if i + l < n:
                dp[i + l] += dp[i]
                dp[i + l] %= mod
            if i + r + 1 < n:
                dp[i + r + 1] -= dp[i]
                dp[i + r + 1] %= mod
    for i in range(n - 1):
        dp[i + 1] += dp[i]
        dp[i + 1] %= mod
    print(dp[n - 1])
