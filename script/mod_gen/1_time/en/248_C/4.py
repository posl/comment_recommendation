def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[[0 for _ in range(K + 1)] for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M):
            for k in range(K):
                dp[i][j][k + 1] += dp[i][j][k]
                dp[i][j + 1][k + 1] += dp[i][j][k]
                dp[i + 1][j + 1][k + 1] += dp[i][j][k]
                dp[i][j][k + 1] %= MOD
                dp[i][j + 1][k + 1] %= MOD
                dp[i + 1][j + 1][k + 1] %= MOD
    print(dp[N][M][K])

if __name__ == '__main__':
    main()