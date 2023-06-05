def dfs(i,j):
    if i<0 or j<0 or i>=1000 or j>=1000:
        return
    if visit[i][j] == 1:
        return
    if grid[i][j] == 0:
        return
    visit[i][j] = 1
    dfs(i-1,j-1)
    dfs(i-1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    dfs(i+1,j)
    dfs(i+1,j+1)
N = int(input())
grid = [[0 for i in range(1000)] for j in range(1000)]
visit = [[0 for i in range(1000)] for j in range(1000)]
for i in range(N):
    x,y = input().split()
    x = int(x)+500
    y = int(y)+500
    grid[x][y] = 1
ans = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] == 1 and visit[i][j] == 0:
            dfs(i,j)
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()