def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j] * M % mod
            if j >= i:
                dp[i][j] = (dp[i][j] + dp[i][j - i]) % mod
    print(dp[N][K])

if __name__ == '__main__':
    main()