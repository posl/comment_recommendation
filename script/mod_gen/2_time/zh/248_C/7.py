def mypow(a,b):
    if b==1:
        return a
    elif b==0:
        return 1
    else:
        c=mypow(a,b//2)
        if b%2==0:
            return c*c
        else:
            return c*c*a
n,m,k=map(int,input().split())
mod=998244353
dp=[[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
dp[0][0][0]=1
for i in range(n):
    for j in range(m+1):
        for l in range(k+1):
            if l+j<=k:
                dp[i+1][j][l+j]+=dp[i][j][l]
                dp[i+1][j][l+j]%=mod
            if l+j+1<=k and j+1<=m:
                dp[i+1][j+1][l+j+1]+=dp[i][j][l]
                dp[i+1][j+1][l+j+1]%=mod
print(dp[n][m][k])

if __name__ == '__main__':
    mypow()