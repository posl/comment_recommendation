def dfs(x,y):
    global visited, black
    visited[x][y] = True
    black.append((x,y))
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 2002 and 0 <= ny < 2002:
            if not visited[nx][ny] and grid[nx][ny] == '#':
                dfs(nx,ny)
N = int(input())
grid = [['.'] * 2002 for _ in range(2002)]
visited = [[False] * 2002 for _ in range(2002)]
dx = [-1,-1,0,0,1,1]
dy = [-1,0,-1,1,0,1]
black = []
for _ in range(N):
    x,y = map(int,input().split())
    x += 1001
    y += 1001
    grid[x][y] = '#'
ans = 0
for i in range(2002):
    for j in range(2002):
        if not visited[i][j] and grid[i][j] == '#':
            dfs(i,j)
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()