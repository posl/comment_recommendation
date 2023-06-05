def dfs(x,y):
    #print(x,y)
    if x < 0 or x >= 1000 or y < 0 or y >= 1000:
        return
    if grid[x][y] == 0:
        return
    if visited[x][y] == 1:
        return
    visited[x][y] = 1
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
N = int(input())
grid = [[0 for _ in range(1000)] for _ in range(1000)]
visited = [[0 for _ in range(1000)] for _ in range(1000)]
for i in range(N):
    x,y = map(int,input().split())
    grid[x][y] = 1
ans = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()