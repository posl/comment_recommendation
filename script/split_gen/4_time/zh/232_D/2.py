def max_square(maze):
    m = len(maze)
    n = len(maze[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] if maze[i][0] == '.' else 0
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] if maze[0][j] == '.' else 0
    for i in range(1, m):
        for j in range(1, n):
            if maze[i][j] == '.':
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
