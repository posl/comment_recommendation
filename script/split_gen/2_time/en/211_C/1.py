def solve():
    s = input()
    n = len(s)
    dp = [[0] * 9 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        dp[i + 1] = dp[i][:]
        if s[i] == 'c':
            dp[i + 1][1] += dp[i][0]
        elif s[i] == 'h':
            dp[i + 1][2] += dp[i][1]
        elif s[i] == 'o':
            dp[i + 1][3] += dp[i][2]
        elif s[i] == 'k':
            dp[i + 1][4] += dp[i][3]
        elif s[i] == 'u':
            dp[i + 1][5] += dp[i][4]
        elif s[i] == 'd':
            dp[i + 1][6] += dp[i][5]
        elif s[i] == 'a':
            dp[i + 1][7] += dp[i][6]
        elif s[i] == 'i':
            dp[i + 1][8] += dp[i][7]
        for j in range(9):
            dp[i + 1][j] %= 10 ** 9 + 7
    print(dp[n][8])
