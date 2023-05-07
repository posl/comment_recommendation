def main():
    N,M,K = map(int,input().split())
    mod = 998244353
    dp = [[[0 for i in range(K+1)] for j in range(M+1)] for k in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= mod
                if k+j <= K:
                    dp[i+1][j][k+j] += dp[i][j][k]
                    dp[i+1][j][k+j] %= mod
                if j+1 <= M:
                    dp[i+1][j+1][k] += dp[i][j][k]
                    dp[i+1][j+1][k] %= mod
    print(dp[N][M][K])

if __name__ == '__main__':
    main()