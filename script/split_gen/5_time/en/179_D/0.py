def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l = max(1, i - R[j])
            r = max(0, i - L[j])
            if r < l:
                continue
            dp[i] += dpsum[r] - dpsum[l - 1]
        dp[i] %= 998244353
        dpsum[i] = dpsum[i - 1] + dp[i]
    print(dp[N])
