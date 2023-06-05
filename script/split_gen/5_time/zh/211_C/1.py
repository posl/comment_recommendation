def solve():
    mod = 10 ** 9 + 7
    s = input()
    n = len(s)
    chokuda = 'chokudai'
    dp = [[0] * 9 for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, 9):
            if s[i - 1] == chokuda[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][8])
