def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dp_cumsum = [0] * (N + 1)
    dp_cumsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            if i - L[j] >= 1:
                dp[i] += dp_cumsum[i - L[j]] - dp_cumsum[max(i - R[j] - 1, 0)]
        dp_cumsum[i] = dp_cumsum[i - 1] + dp[i]
    print(dp[N] % mod)
