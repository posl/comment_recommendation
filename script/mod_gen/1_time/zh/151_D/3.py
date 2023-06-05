def dfs(x, y, cnt):
    global ans
    if cnt > ans:
        ans = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == '.' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = 0
h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            visited[i][j] = 1
            dfs(i, j, 0)
            visited[i][j] = 0
print(ans)

if __name__ == '__main__':
    dfs()