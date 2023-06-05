def dfs(i, j):
    global visited, black
    visited[i][j] = True
    for k in range(6):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 2001 and 0 <= nj < 2001:
            if black[ni][nj] == 1 and not visited[ni][nj]:
                dfs(ni, nj)
n = int(input())
di = [-1, -1, 0, 0, 1, 1]
dj = [-1, 0, -1, 1, 0, 1]
black = [[0] * 2001 for _ in range(2001)]
visited = [[False] * 2001 for _ in range(2001)]
for _ in range(n):
    x, y = map(int, input().split())
    black[x + 1000][y + 1000] = 1
ans = 0
for i in range(2001):
    for j in range(2001):
        if black[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            ans += 1
print(ans)
