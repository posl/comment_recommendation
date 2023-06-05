def dfs(x, y):
    global ans
    ans += 1
    field[x][y] = '#'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and field[nx][ny]=='.':
            dfs(nx, ny)
h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0
dfs(0, 0)
print(ans)

if __name__ == '__main__':
    dfs()