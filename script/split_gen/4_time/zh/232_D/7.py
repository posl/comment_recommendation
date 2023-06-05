def f(h, w, s):
    dp = [[0 for i in range(w)] for j in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[h - 1][w - 1]
