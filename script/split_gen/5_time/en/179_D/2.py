def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for _ in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    MOD = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    dpsum = [0] * (N+1)
    dpsum[1] = 1
    for i in range(2, N+1):
        for j in range(K):
            l = max(0, i-R[j])
            r = max(0, i-L[j]+1)
            dp[i] += (dpsum[r] - dpsum[l]) % MOD
        dpsum[i] = dpsum[i-1] + dp[i]
    print(dp[N] % MOD)
