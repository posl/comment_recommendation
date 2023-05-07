def main():
    N, M, K = map(int, input().split())
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for n in range(N):
        for m in range(M+1):
            for k in range(K+1):
                dp[n+1][m][k] += dp[n][m][k] * (m+1)
                dp[n+1][m][k] %= 998244353
                if k + m + 1 <= K:
                    dp[n+1][m+1][k+m+1] += dp[n][m][k]
                    dp[n+1][m+1][k+m+1] %= 998244353
    print(dp[N][M][K])

if __name__ == '__main__':
    main()