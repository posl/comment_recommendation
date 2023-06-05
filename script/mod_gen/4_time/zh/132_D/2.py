def main():
    n,k = map(int,input().split())
    MOD = 10**9+7
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        dp[i][0] = 1
        for j in range(1,i+1):
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])%MOD
    for i in range(k):
        ans = (dp[k-1][i]*dp[n-k+1][i])%MOD
        print(ans)

if __name__ == '__main__':
    main()