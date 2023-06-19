def dfs(h,w,k):
    #print(h,w,k)
    if h==0:
        return 1
    if dp[h][w][k]!=-1:
        return dp[h][w][k]
    if k==1:
        dp[h][w][k]=dfs(h-1,w,k)+dfs(h-1,w+1,k+1)
    elif k==w:
        dp[h][w][k]=dfs(h-1,w-1,k-1)+dfs(h-1,w,k)
    else:
        dp[h][w][k]=dfs(h-1,w-1,k-1)+dfs(h-1,w,k)+dfs(h-1,w+1,k+1)
    dp[h][w][k]%=1000000007
    return dp[h][w][k]
H,W,K=map(int,input().split())
dp=[[[-1 for _ in range(W+2)] for _ in range(W+2)] for _ in range(H+1)]
print(dfs(H,W,K))
