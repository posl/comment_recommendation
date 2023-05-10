def main():
    n,m,k=map(int,input().split())
    mod=998244353
    dp=[[[0 for i in range(k+1)] for j in range(m+1)] for k in range(n+1)]
    dp[0][0][0]=1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l]+=dp[i][j][l]*(m-j)
                dp[i+1][j][l]%=mod
                if l+j+1<=k:
                    dp[i+1][j+1][l+j+1]+=dp[i][j][l]
                    dp[i+1][j+1][l+j+1]%=mod
    print(dp[n][m][k])
