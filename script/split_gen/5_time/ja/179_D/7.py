def solve():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dp_sum = [0] * (N + 1)
    dp_sum[1] = 1
    for i in range(2, N + 1):
        for L, R in LRs:
            l = max(1, i - R)
            r = i - L
            if r < 0:
                continue
            dp[i] += dp_sum[r] - dp_sum[l - 1]
            dp[i] %= MOD
        dp_sum[i] = dp_sum[i - 1] + dp[i]
        dp_sum[i] %= MOD
    print(dp[N])
