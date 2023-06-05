def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(i+1):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= mod
    for i in range(1,k+1):
        ans = dp[n-k][i]*dp[k][i]%mod
        print(ans)
