def main():
    n,m,k=map(int,input().split())
    mod=998244353
    dp=[[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0]=1
    for i in range(n):
        for j in range(m+1):
            for s in range(k+1):
                dp[i+1][j][s]+=dp[i][j][s]
                dp[i+1][j][s]%=mod
                if s+j<=k:
                    dp[i+1][j][s+j]+=dp[i][j][s]
                    dp[i+1][j][s+j]%=mod
    print(dp[n][m][k])

if __name__ == '__main__':
    main()