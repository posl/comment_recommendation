def main():
    n,k=map(int,input().split())
    mod=10**9+7
    dp=[[0 for i in range(n+1)]for j in range(n+1)]
    dp[0][0]=1
    for i in range(n):
        for j in range(i+1):
            dp[i+1][j+1]=(dp[i+1][j+1]+dp[i][j])%mod
            dp[i+1][j]=(dp[i+1][j]+dp[i][j]*(i-j))%mod
    for i in range(1,k+1):
        print(dp[n-k][i]*dp[k-1][i-1]%mod)
