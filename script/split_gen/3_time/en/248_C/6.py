def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[[0] * (K + 1) for i in range(M + 1)] for j in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(M + 1):
            for k in range(K + 1):
                for l in range(j + 1):
                    if k + l <= K:
                        dp[i + 1][j][k + l] += dp[i][j - l][k]
                        dp[i + 1][j][k + l] %= mod
    print(sum(dp[N][M]) % mod)
