def dfs(y, x, d):
    global ans
    ans = max(ans, d)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (ny < 0 or ny >= h or nx < 0 or nx >= w):
            continue
        if (s[ny][nx] == '#'):
            continue
        if (visited[ny][nx]):
            continue
        visited[ny][nx] = True
        dfs(ny, nx, d + 1)
        visited[ny][nx] = False
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
ans = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(h):
    for j in range(w):
        if (s[i][j] == '#'):
            continue
        visited = [[False] * w for _ in range(h)]
        visited[i][j] = True
        dfs(i, j, 0)
print(ans)

if __name__ == '__main__':
    dfs()