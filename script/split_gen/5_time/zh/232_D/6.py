def dfs(i, j):
    global ans
    if i == h - 1 and j == w - 1:
        ans += 1
        return
    if i + 1 < h and maze[i + 1][j] == '.':
        dfs(i + 1, j)
    if j + 1 < w and maze[i][j + 1] == '.':
        dfs(i, j + 1)
h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
ans = 0
dfs(0, 0)
print(ans)
