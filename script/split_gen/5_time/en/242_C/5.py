def main():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 10 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(10):
            for k in range(j-1, j+2):
                if k < 0 or k > 9:
                    continue
                dp[i][j] += dp[i-1][k]
                dp[i][j] %= MOD
    print(sum(dp[N]) % MOD)
