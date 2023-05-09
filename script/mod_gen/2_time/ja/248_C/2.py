def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (M-1) % MOD
            if j >= i:
                dp[i][j] = (dp[i][j] - dp[i-1][j-i] * (M-2)) % MOD
    print(dp[N][K])

if __name__ == '__main__':
    main()