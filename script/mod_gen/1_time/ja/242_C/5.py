def main():
    MOD = 998244353
    N = int(input())
    dp = [[0] * 10 for _ in range(N)]
    dp[0][1] = 1
    for i in range(1, N):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = (dp[i-1][0] + dp[i-1][1]) % MOD
        dp[i][2] = (dp[i-1][1] + dp[i-1][2]) % MOD
        dp[i][3] = (dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][4] = (dp[i-1][3] + dp[i-1][4]) % MOD
        dp[i][5] = (dp[i-1][4] + dp[i-1][5]) % MOD
        dp[i][6] = (dp[i-1][5] + dp[i-1][6]) % MOD
        dp[i][7] = (dp[i-1][6] + dp[i-1][7]) % MOD
        dp[i][8] = (dp[i-1][7] + dp[i-1][8]) % MOD
        dp[i][9] = dp[i-1][8]
    print(sum(dp[N-1]) % MOD)
main()

if __name__ == '__main__':
    main()