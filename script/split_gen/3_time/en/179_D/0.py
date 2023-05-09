def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    dp = [0] * (N + 1)
    dp[1] = 1
    dp_sum = [0] * (N + 1)
    dp_sum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            if i - L[j] <= 0:
                continue
            if i - R[j] <= 0:
                dp[i] += dp_sum[i - L[j]]
            else:
                dp[i] += dp_sum[i - L[j]] - dp_sum[i - R[j] - 1]
            dp[i] %= 998244353
        dp_sum[i] = dp_sum[i - 1] + dp[i]
        dp_sum[i] %= 998244353
    print(dp[N])
