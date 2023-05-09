def main():
    # Take input Here and Call solution function
    h,w = get_ints_in_variables()
    grid = [get_string() for _ in range(h)]
    # print(grid)
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1 if grid[0][0] == '.' else 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                if i > 0 and grid[i-1][j] == '.':
                    dp[i][j] = dp[i-1][j]
                if j > 0 and grid[i][j-1] == '.':
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= mod
    print(dp[h-1][w-1])

if __name__ == '__main__':
    main()