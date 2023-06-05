def dfs(x,y):
    global ans
    ans = max(ans, dist[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and s[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            dfs(nx,ny)
            dist[nx][ny] = -1
h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        dist = [[-1] * w for i in range(h)]
        dist[i][j] = 0
        dfs(i,j)
print(ans)

if __name__ == '__main__':
    dfs()