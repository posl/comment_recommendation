def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(list(input()))
    dp = [[0 for i in range(W)] for j in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == ".":
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
    print(dp[H - 1][W - 1] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()