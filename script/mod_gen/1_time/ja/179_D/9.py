def main():
    N, K = map(int, input().split())
    L, R = zip(*[map(int, input().split()) for _ in range(K)])
    L, R = list(L), list(R)
    MOD = 998244353
    dp = [0] * (N + 1)  # dp[i] = i番目のマスにたどり着く経路の数
    dp[1] = 1
    dp_sum = [0] * (N + 1)  # dp_sum[i] = dp[1] + dp[2] + ... + dp[i]
    dp_sum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            dp[i] += dp_sum[max(i - R[j], 0)] - dp_sum[max(i - L[j], 0)]
        dp[i] %= MOD
        dp_sum[i] = (dp_sum[i - 1] + dp[i]) % MOD
    print(dp[N])

if __name__ == '__main__':
    main()