def solve():
    N, K = map(int, input().split())
    L = []
    R = []
    for _ in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    MOD = 998244353
    dp = [0] * N
    dp[0] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(1, N):
        for j in range(K):
            dp[i] += dpsum[max(i - L[j], 0)] - dpsum[max(i - R[j] - 1, 0)]
            dp[i] %= MOD
        dpsum[i + 1] = dpsum[i] + dp[i]
        dpsum[i + 1] %= MOD
    print(dp[N - 1])
solve()
