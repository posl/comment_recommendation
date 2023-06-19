def func():
    n,m,k=map(int,input().split())
    dp=[[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0]=1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                dp[i+1][j][l]+=dp[i][j][l]
                dp[i+1][j][l]%=998244353
                if l+j<=k:
                    dp[i+1][j][l+j]+=dp[i][j][l]
                    dp[i+1][j][l+j]%=998244353
    ans=0
    for j in range(m+1):
        ans+=dp[n][j][k]
        ans%=998244353
    print(ans)

if __name__ == '__main__':
    func()