def dfs(x, y, c):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if g[x][y] != 1:
        return
    g[x][y] = c
    dfs(x - 1, y - 1, c)
    dfs(x - 1, y, c)
    dfs(x, y - 1, c)
    dfs(x, y + 1, c)
    dfs(x + 1, y, c)
    dfs(x + 1, y + 1, c)
n = int(input())
g = [[0] * 2000 for _ in range(2000)]
for _ in range(n):
    x, y = map(int, input().split())
    g[x + 1000][y + 1000] = 1
c = 2
for i in range(2000):
    for j in range(2000):
        if g[i][j] == 1:
            dfs(i, j, c)
            c += 1
count = [0] * 2000000
for i in range(2000):
    for j in range(2000):
        if g[i][j] > 0:
            count[g[i][j]] += 1
ans = 0
for i in range(len(count)):
    if count[i] > 0:
        ans += 1
print(ans - 1)
