def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    #print(grid)
    dp = [[0] * (W+1) for i in range(H+1)]
    dp[1][1] = 1
    for i in range(1, H+1):
        for j in range(1, W+1):
            if grid[i-1][j-1] == ".":
                dp[i][j] = max(dp[i][j], dp[i-1][j] + dp[i][j-1])
    print(dp[H][W])

if __name__ == '__main__':
    main()