def solve(H, W, C):
    #dp[i][j]表示从(i, j)开始的最大路径数
    dp = [[0 for j in range(W)] for i in range(H)]
    dp[H - 1][W - 1] = 1
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if C[i][j] == '#':
                continue
            if i + 1 < H:
                dp[i][j] = (dp[i][j] + dp[i + 1][j]) % 1000000007
            if j + 1 < W:
                dp[i][j] = (dp[i][j] + dp[i][j + 1]) % 1000000007
    return dp[0][0]
