def main():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 2 for _ in range(N + 1)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1, N + 1):
        dp[i][0] = (dp[i - 1][0] * 9 + dp[i - 1][1] * 9) % MOD
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
    print((dp[N][0] + dp[N][1]) % MOD)
