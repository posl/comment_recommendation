def main():
    N, M, K = map(int, input().split())
    dp = [[[0] * (K+1) for _ in range(M+1)] for __ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M+1):
            for k in range(K+1):
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j][k] %= 998244353
                if j+1 <= M and k+i+1 <= K:
                    dp[i+1][j+1][k+i+1] += dp[i][j][k]
                    dp[i+1][j+1][k+i+1] %= 998244353
    print(dp[N][M][K])
