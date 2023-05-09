def main():
    N, K = map(int, input().split())
    S = []
    for i in range(K):
        L, R = map(int, input().split())
        S.append((L, R))
    dp = [0] * (N + 1)
    dp_sum = [0] * (N + 1)
    dp[1] = 1
    dp_sum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            L, R = S[j]
            dp[i] += dp_sum[max(i - L, 0)] - dp_sum[max(i - R - 1, 0)]
            dp[i] %= 998244353
        dp_sum[i] = dp_sum[i - 1] + dp[i]
    print(dp[N])

if __name__ == '__main__':
    main()