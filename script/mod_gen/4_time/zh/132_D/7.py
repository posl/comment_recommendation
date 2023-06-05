def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0 for _ in range(n+1)] for _ in range(k)]
    dp[0][0] = 1
    for i in range(1,k):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            dp[i][j] %= mod
    for i in range(1,k+1):
        print(dp[i-1][n-k+1]*dp[k-i][k-1]%mod)

if __name__ == '__main__':
    main()