def solve(h,w,c):
    dp = [[0 for _ in range(w)] for _ in range(h)]
    if c[0][0] == '#':
        dp[0][0] = 0
    else:
        dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if c[i][j] == '#':
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[h-1][w-1]

if __name__ == '__main__':
    solve()