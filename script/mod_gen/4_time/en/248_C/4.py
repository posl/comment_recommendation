def main():
    n,m,k=[int(i) for i in input().split()]
    dp=[[[0 for i in range(k+1)] for j in range(m+1)] for k in range(n+1)]
    dp[0][0][0]=1
    mod=998244353
    for i in range(n):
        for j in range(m+1):
            for k in range(k+1):
                dp[i+1][j][k]+=dp[i][j][k]
                dp[i+1][j][k]%=mod
                if k+j<=k:
                    dp[i+1][j][k+j]+=dp[i][j][k]
                    dp[i+1][j][k+j]%=mod
    print(dp[n][m][k])
main()

if __name__ == '__main__':
    main()