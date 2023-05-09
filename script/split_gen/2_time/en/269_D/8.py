def main():
    N = int(input())
    # 2D array
    grid = [[0 for x in range(2001)] for y in range(2001)]
    for i in range(N):
        X, Y = map(int, input().split())
        X += 1000
        Y += 1000
        grid[X][Y] = 1
    def dfs(x, y):
        if x < 0 or 2000 < x or y < 0 or 2000 < y or grid[x][y] == 0:
            return
        grid[x][y] = 0
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
    ans = 0
    for i in range(2001):
        for j in range(2001):
            if grid[i][j] == 1:
                dfs(i, j)
                ans += 1
    print(ans)
