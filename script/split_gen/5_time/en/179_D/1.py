def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    mod = 998244353
    dp = [0]*(N+1)
    dp[1] = 1
    dpsum = [0]*(N+1)
    dpsum[1] = 1
    for i in range(2, N+1):
        for j in range(K):
            if i-L[j] < 1:
                continue
            dp[i] += dpsum[i-L[j]] - dpsum[max(i-R[j]-1, 0)]
            dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod
    print(dp[N])
