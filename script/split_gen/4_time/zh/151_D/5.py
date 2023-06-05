def dfs(x,y):
    global ans
    ans = max(ans, dist[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and c[nx][ny] == '.' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            dfs(nx, ny)
            dist[nx][ny] = -1
h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
dist = [[-1]*w for _ in range(h)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == '.':
            dist = [[-1]*w for _ in range(h)]
            dist[i][j] = 0
            dfs(i,j)
print(ans)
