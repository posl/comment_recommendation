def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    for k in range(K + 1):
        for n in range(N + 1):
            for m in range(1, M + 1):
                if k + m > K or n + 1 > N:
                    continue
                dp[k + m][n + 1] += dp[k][n]
                dp[k + m][n + 1] %= MOD
    print(dp[K][N])
