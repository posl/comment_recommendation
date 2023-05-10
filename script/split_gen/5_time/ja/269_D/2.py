def dfs(x, y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000 or grid[x][y] == 0:
        return
    grid[x][y] = 0
    dfs(x-1, y-1)
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x+1, y)
    dfs(x+1, y+1)
n = int(input())
grid = [[0]*2000 for _ in range(2000)]
for _ in range(n):
    x, y = map(int, input().split())
    grid[x+1000][y+1000] = 1
ans = 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)
