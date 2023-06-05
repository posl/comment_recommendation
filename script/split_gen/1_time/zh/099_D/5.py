def solve(n,c,d,cmap):
    #dp[i][j]表示前i个格子，第i个格子涂成颜色j的最小代价
    dp = [[float('inf') for i in range(c)] for j in range(n)]
    for i in range(c):
        dp[0][i] = d[i][cmap[0]-1]
    for i in range(1,n):
        for j in range(c):
            for k in range(c):
                if (i+j)%3 == (k+cmap[i]-1)%3:
                    dp[i][k] = min(dp[i][k],dp[i-1][j]+d[k][cmap[i]-1])
    return min(dp[n-1])
n,c = map(int,input().split())
d = []
for i in range(c):
    d.append(list(map(int,input().split())))
cmap = []
for i in range(n):
    cmap.extend(list(map(int,input().split())))
print(solve(n,c,d,cmap))
