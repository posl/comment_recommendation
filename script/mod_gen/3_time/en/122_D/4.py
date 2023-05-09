def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[0]*4 for _ in range(N+1)]
    for i in range(4):
        dp[3][i] = 1
    for i in range(4, N+1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3]) % MOD
        dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % MOD
    ans = 0
    for i in range(4):
        ans += dp[N][i]
    print(ans%MOD)

if __name__ == '__main__':
    main()