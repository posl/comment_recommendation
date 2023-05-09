def main():
    h,w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1 if grid[0][0] == '.' else 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
    print(dp[h-1][w-1])
