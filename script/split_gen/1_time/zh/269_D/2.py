def dfs(i,j):
    if i < 0 or i >= 2000 or j < 0 or j >= 2000:
        return
    if color[i][j] == 0:
        return
    if visited[i][j]:
        return
    visited[i][j] = True
    dfs(i-1,j-1)
    dfs(i-1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    dfs(i+1,j)
    dfs(i+1,j+1)
n = int(input())
color = [[0]*2000 for i in range(2000)]
visited = [[False]*2000 for i in range(2000)]
for i in range(n):
    x,y = map(int,input().split())
    x += 1000
    y += 1000
    color[x][y] = 1
ans = 0
for i in range(2000):
    for j in range(2000):
        if color[i][j] == 1 and not visited[i][j]:
            dfs(i,j)
            ans += 1
print(ans)
