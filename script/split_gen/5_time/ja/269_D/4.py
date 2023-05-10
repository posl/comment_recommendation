def dfs(i, j, visited):
    if visited[i][j] == True:
        return
    visited[i][j] = True
    for k in range(6):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 2001 and 0 <= nj < 2001:
            dfs(ni, nj, visited)
N = int(input())
di = [-1, -1, 0, 0, 1, 1]
dj = [-1, 0, -1, 1, 0, 1]
visited = [[False] * 2001 for _ in range(2001)]
for _ in range(N):
    x, y = map(int, input().split())
    visited[x + 1000][y + 1000] = True
ans = 0
for i in range(2001):
    for j in range(2001):
        if visited[i][j] == True:
            dfs(i, j, visited)
            ans += 1
print(ans)
