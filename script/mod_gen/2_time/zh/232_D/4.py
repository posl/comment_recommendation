def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= h or ny >= w or nx < 0 or ny < 0:
            continue
        if graph[nx][ny] == '#':
            continue
        if visited[nx][ny]:
            continue
        dfs(nx, ny)
h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
dfs(0, 0)
ans = 0
for i in range(h):
    for j in range(w):
        if visited[i][j]:
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()