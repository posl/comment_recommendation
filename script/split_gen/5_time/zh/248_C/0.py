def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= MOD
                if j < M and k + j <= K:
                    dp[i+1][j+1][k+j] += dp[i][j][k]
                    dp[i+1][j+1][k+j] %= MOD
    print(dp[N][M][K])
