def dfs(now,visited):
    if visited==2**n-1:
        if now==0:
            return 1
        else:
            return 0
    elif now in dp and visited in dp[now]:
        return dp[now][visited]
    else:
        ans=0
        for i in range(n):
            if visited>>i&1==0:
                ans+=dfs(i,visited|1<<i)
        if now in dp:
            dp[now][visited]=ans
        else:
            dp[now]={visited:ans}
        return ans
n,k=map(int,input().split())
t=[list(map(int,input().split())) for i in range(n)]
dp={}
print(dfs(0,1))
