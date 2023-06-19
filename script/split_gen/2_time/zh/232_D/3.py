def dfs(i, j):
    global H, W, ans, grid
    # print(i, j)
    ans += 1
    grid[i][j] = "#"
    if i + 1 < H and grid[i + 1][j] == ".":
        dfs(i + 1, j)
    if j + 1 < W and grid[i][j + 1] == ".":
        dfs(i, j + 1)
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
ans = 0
dfs(0, 0)
print(ans)
