def dfs(h,w,k):
    if dp[h][w][k] != -1:
        return dp[h][w][k]
    if h == 0:
        if k == 0:
            dp[h][w][k] = 1
        else:
            dp[h][w][k] = 0
    elif k == 0:
        dp[h][w][k] = dfs(h-1,w-1,0) + dfs(h-1,w,1)*(w-1)
    else:
        dp[h][w][k] = dfs(h-1,w-1,k-1) + dfs(h-1,w,k)*(w-k) + dfs(h-1,w,k+1)*(k+1)
    dp[h][w][k] %= 1000000007
    return dp[h][w][k]
h,w,k = map(int,input().split())
dp = [[[-1 for _ in range(w+1)] for _ in range(w+1)] for _ in range(h+1)]
print(dfs(h,w,k))
