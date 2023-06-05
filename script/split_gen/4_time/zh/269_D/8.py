def dfs(x,y):
    if x<0 or x>=1001 or y<0 or y>=1001:
        return
    if visited[x][y]:
        return
    if not grid[x][y]:
        return
    visited[x][y]=True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
N=int(input())
grid=[[False]*1001 for _ in range(1001)]
visited=[[False]*1001 for _ in range(1001)]
for _ in range(N):
    x,y=map(int,input().split())
    grid[x][y]=True
ans=0
for i in range(1001):
    for j in range(1001):
        if not visited[i][j] and grid[i][j]:
            dfs(i,j)
            ans+=1
print(ans)
