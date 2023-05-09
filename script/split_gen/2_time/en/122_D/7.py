def main():
    N = int(input())
    MOD = 10**9+7
    # AGC, ACG, GAC, AC?, AG?, CG?
    dp = [[1, 1, 1, 1, 1, 1, 1] for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][5] + dp[i-1][6]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][4]) % MOD
        dp[i][2] = (dp[i-1][1] + dp[i-1][3] + dp[i-1][4]) % MOD
        dp[i][3] = (dp[i-1][2] + dp[i-1][6]) % MOD
        dp[i][4] = (dp[i-1][1] + dp[i-1][5]) % MOD
        dp[i][5] = (dp[i-1][2] + dp[i-1][6]) % MOD
        dp[i][6] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4] + dp[i-1][5]) % MOD
    print(sum(dp[N])%MOD)
