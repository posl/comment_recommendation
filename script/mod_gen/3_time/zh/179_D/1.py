def solve():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for l, r in LR:
            dp[i] += dpsum[max(0, i - l)] - dpsum[max(0, i - r - 1)]
            dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])
solve()
