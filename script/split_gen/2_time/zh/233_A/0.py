def dfs(i,j):
    if i == h - 1 and j == w - 1:
        return 1
    if visited[i][j]:
        return dp[i][j]
    visited[i][j] = True
    if i < h - 1 and maze[i+1][j] != '#':
        dp[i][j] += dfs(i+1,j)
    if j < w - 1 and maze[i][j+1] != '#':
        dp[i][j] += dfs(i,j+1)
    return dp[i][j]
h,w = map(int,input().split())
maze = [list(input()) for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]
dp = [[0 for _ in range(w)] for _ in range(h)]
print(dfs(0,0))
