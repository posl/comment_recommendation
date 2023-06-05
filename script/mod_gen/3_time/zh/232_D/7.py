def dfs(x, y):
    global ans
    ans += 1
    maze[x][y] = '#'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx) and (nx < H) and (0 <= ny) and (ny < W) and (maze[nx][ny] == '.'):
            dfs(nx, ny)
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0
dfs(0, 0)
print(ans)

if __name__ == '__main__':
    dfs()