def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            for k in range(1, M + 1):
                if j + k <= K:
                    dp[i][j + k] = (dp[i][j + k] + dp[i - 1][j]) % MOD
    print(dp[N][K])
