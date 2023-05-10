def solve():
    #n, a, b = map(int, input().split())
    #s = input()
    n, a, b = 5, 1, 2
    s = 'rrefa'
    print(n, a, b)
    print(s)
    #dp = [[0] * n for _ in range(n)]
    #for i in range(n):
    #    dp[i][i] = 0
    #for i in range(n - 1):
    #    dp[i][i + 1] = 0 if s[i] == s[i + 1] else 1
    #for i in range(3, n):
    #    for j in range(n - i):
    #        if s[j] == s[j + i]:
    #            dp[j][j + i] = dp[j + 1][j + i - 1]
    #        else:
    #            dp[j][j + i] = min(dp[j + 1][j + i] + 1, dp[j][j + i - 1] + 1)
    #print(dp[0][n - 1])
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n - 1):
        dp[i][i + 1] = 0 if s[i] == s[i + 1] else 1
    for i in range(3, n):
        for j in range(n - i):
            if s[j] == s[j + i]:
                dp[j][j + i] = dp[j + 1][j + i - 1]
            else:
                dp[j][j + i] = min(dp[j + 1][j + i] + 1, dp[j][j + i - 1] + 1)
    print(dp[0][n - 1])
