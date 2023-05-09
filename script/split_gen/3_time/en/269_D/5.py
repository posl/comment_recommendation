def dfs(i,j):
    global visited
    visited[i][j] = True
    for k in range(6):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 2001 and 0 <= nj < 2001 and visited[ni][nj] == False and grid[ni][nj] == '#':
            dfs(ni,nj)
N = int(input())
grid = [['.'] * 2001 for _ in range(2001)]
di = [-1,-1,0,0,1,1]
dj = [-1,0,-1,1,0,1]
for _ in range(N):
    X,Y = map(int,input().split())
    grid[X+1000][Y+1000] = '#'
visited = [[False] * 2001 for _ in range(2001)]
ans = 0
for i in range(2001):
    for j in range(2001):
        if visited[i][j] == False and grid[i][j] == '#':
            ans += 1
            dfs(i,j)
print(ans)
