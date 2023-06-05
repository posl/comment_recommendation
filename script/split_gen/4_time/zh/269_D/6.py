def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return
    if a[x][y] == 0:
        return
    a[x][y] = 0
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
    dfs(x-1,y-1)
n = int(input())
a = [[0]*n for _ in range(n)]
for _ in range(n):
    x,y = map(int,input().split())
    a[x][y] = 1
ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            dfs(i,j)
            ans += 1
print(ans)
