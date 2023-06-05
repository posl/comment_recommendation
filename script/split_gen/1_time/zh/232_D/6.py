def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 if grid[0][0] == '.' else 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[-1][-1])
