def dfs(x, y):
    if x == h - 1 and y == w - 1:
        return 1
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == '#':
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = dfs(x + 1, y) + dfs(x, y + 1)
    return dp[x][y]
h, w = map(int, input().split())
c = [input() for _ in range(h)]
dp = [[-1] * w for _ in range(h)]
print(dfs(0, 0))
