def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            for k in range(i, K + 1):
                dp[i][k] += dp[i - 1][k - j]
                dp[i][k] %= mod
    print(dp[N][K])
