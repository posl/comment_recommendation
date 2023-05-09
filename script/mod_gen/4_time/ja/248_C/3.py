def main():
    n,m,k=map(int,input().split())
    mod=998244353
    dp=[[[0]*(k+1) for i in range(m+1)] for j in range(n+1)]
    dp[0][0][0]=1
    for i in range(n+1):
        for j in range(m+1):
            for l in range(k+1):
                if i>0 and l>=j:
                    dp[i][j][l]+=dp[i-1][j][l-j]
                    dp[i][j][l]%=mod
                if j>0:
                    dp[i][j][l]+=dp[i][j-1][l]
                    dp[i][j][l]%=mod
    print(dp[n][m][k])

if __name__ == '__main__':
    main()