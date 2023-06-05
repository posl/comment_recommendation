def dfs(i,j):
    if i<0 or i>=1001 or j<0 or j>=1001:
        return
    if visited[i][j] == 1:
        return
    if grid[i][j] == 0:
        return
    visited[i][j] = 1
    dfs(i-1,j-1)
    dfs(i-1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    dfs(i+1,j)
    dfs(i+1,j+1)
    return
N = int(input())
grid = [[0 for i in range(1001)] for j in range(1001)]
visited = [[0 for i in range(1001)] for j in range(1001)]
for i in range(N):
    x,y = map(int,input().split())
    grid[x+500][y+500] = 1
count = 0
for i in range(1001):
    for j in range(1001):
        if visited[i][j] == 0 and grid[i][j] == 1:
            dfs(i,j)
            count += 1
print(count)

if __name__ == '__main__':
    dfs()