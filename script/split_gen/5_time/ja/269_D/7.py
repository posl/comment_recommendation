def dfs(x, y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if c[y][x] == 0:
        return
    if visited[y][x]:
        return
    visited[y][x] = True
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)
n = int(input())
c = [[0 for _ in range(2000)] for _ in range(2000)]
visited = [[False for _ in range(2000)] for _ in range(2000)]
for _ in range(n):
    x, y = map(int, input().split())
    c[y + 1000][x + 1000] = 1
ans = 0
for i in range(2000):
    for j in range(2000):
        if c[i][j] == 1 and visited[i][j] == False:
            ans += 1
            dfs(j, i)
print(ans)
