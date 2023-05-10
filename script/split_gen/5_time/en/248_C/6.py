def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        ndp = [0] * (K + 1)
        for j in range(1, M + 1):
            for k in range(K - j, -1, -1):
                ndp[k + j] += dp[k]
                ndp[k + j] %= MOD
        dp = ndp
    print(dp[K])
