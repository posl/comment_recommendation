def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for k in range(K):
            li = max(1, i - R[k])
            ri = max(0, i - L[k] - 1)
            dp[i] += dpsum[ri] - dpsum[li - 1]
        dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])
