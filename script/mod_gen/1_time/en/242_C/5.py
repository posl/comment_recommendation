def main():
    N = int(input())
    mod = 998244353
    dp = [[0,0,0] for i in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod
    print((dp[N][0] + dp[N][1] + dp[N][2]) % mod)

if __name__ == '__main__':
    main()