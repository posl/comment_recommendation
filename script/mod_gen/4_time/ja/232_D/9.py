def main():
    H,W = map(int,input().split())
    grid = [[0]*(W+1) for i in range(H+1)]
    for i in range(H):
        grid[i] = list(input())
    dp = [[0]*(W+1) for i in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                continue
            if i+1 < H and grid[i+1][j] == ".":
                dp[i+1][j] += dp[i][j]
            if j+1 < W and grid[i][j+1] == ".":
                dp[i][j+1] += dp[i][j]
    print(dp[H-1][W-1])

if __name__ == '__main__':
    main()