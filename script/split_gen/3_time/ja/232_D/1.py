def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if i > 0 and grid[i - 1][j] == '.':
                dp[i][j] += dp[i - 1][j]
            if j > 0 and grid[i][j - 1] == '.':
                dp[i][j] += dp[i][j - 1]
    print(dp[h - 1][w - 1])
