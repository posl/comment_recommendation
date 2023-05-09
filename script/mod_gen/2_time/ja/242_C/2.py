def main():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = 9
    dp[0][1] = 1
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] * 9 + dp[i-1][1] * 9
        dp[i][1] = dp[i-1][0] + dp[i-1][1]
        dp[i][0] %= MOD
        dp[i][1] %= MOD
    print((dp[N-1][0] + dp[N-1][1]) % MOD)

if __name__ == '__main__':
    main()