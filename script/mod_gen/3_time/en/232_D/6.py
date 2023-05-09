def count():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    return dp[H-1][W-1]
print(count())

if __name__ == '__main__':
    count()