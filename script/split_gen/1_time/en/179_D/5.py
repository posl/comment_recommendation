def solve():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[1] = 1
    sumdp = [0] * (N + 1)
    sumdp[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l = max(1, i - R[j])
            r = max(1, i - L[j])
            dp[i] += sumdp[r] - sumdp[l - 1]
        dp[i] %= 998244353
        sumdp[i] = sumdp[i - 1] + dp[i]
    print(dp[N])
solve()
