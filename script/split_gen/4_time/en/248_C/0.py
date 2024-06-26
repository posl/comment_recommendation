def main():
    N, M, K = map(int, input().split())
    dp = [[[0 for _ in range(K + 1)] for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M):
            for k in range(K + 1):
                dp[i + 1][j + 1][k] += dp[i][j][k]
                dp[i + 1][j + 1][k] %= 998244353
                if k + j + 1 <= K:
                    dp[i + 1][j + 1][k + j + 1] += dp[i][j][k]
                    dp[i + 1][j + 1][k + j + 1] %= 998244353
    print(dp[N][M][K])
