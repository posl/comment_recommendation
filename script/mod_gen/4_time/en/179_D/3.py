def solve():
    N, K = map(int, input().split())
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l, r = map(int, input().split())
            dp[i] += dp[max(0, i - l)] - dp[max(0, i - r - 1)]
            dp[i] %= MOD
    print(dp[N])
solve()
