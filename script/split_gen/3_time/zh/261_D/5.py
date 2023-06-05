def solve():
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    c=[]
    y=[]
    for i in range(m):
        c_,y_=map(int,input().split())
        c.append(c_)
        y.append(y_)
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m):
        for j in range(n+1):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j])
            if j+c[i]<=n:
                dp[i+1][j+c[i]]=max(dp[i+1][j+c[i]],dp[i][j]+y[i])
    ans=0
    for i in range(n+1):
        ans=max(ans,dp[m][i]+x[i-1])
    print(ans)
