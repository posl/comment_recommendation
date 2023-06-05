def solve(n,k,v):
    dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+v[i-1])
            dp[i][j][1] = max(dp[i-1][j-1][1],dp[i-1][j-1][0]-v[i-1])
    return dp[n][k][0]
n,k = map(int,input().split())
v = list(map(int,input().split()))
print(solve(n,k,v))
