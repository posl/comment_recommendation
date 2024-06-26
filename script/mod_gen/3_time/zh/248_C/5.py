def solve(N,M,K):
    dp = [[[0 for i in range(K+1)] for j in range(M+1)] for k in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                if k+j <= K:
                    dp[i+1][j][k+j] = (dp[i+1][j][k+j] + dp[i][j][k]) % 998244353
                if j < M:
                    dp[i+1][j+1][k] = (dp[i+1][j+1][k] + dp[i][j][k]) % 998244353
    return dp[N][M][K]

if __name__ == '__main__':
    solve()