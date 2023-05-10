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
        for j in range(K):
            li = max(0, i - R[j])
            ri = max(0, i - L[j] + 1)
            dp[i] += dpsum[ri] - dpsum[li]
            dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])

if __name__ == '__main__':
    main()