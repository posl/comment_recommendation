def main():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(1, 10):
                if j == 1 or k > 1:
                    dp[i + 1][1] += dp[i][j]
                    dp[i + 1][1] %= MOD
                else:
                    dp[i + 1][0] += dp[i][j]
                    dp[i + 1][0] %= MOD
    print((dp[N][0] + dp[N][1]) % MOD)
