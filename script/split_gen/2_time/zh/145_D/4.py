def knight(x, y):
    mod = 10 ** 9 + 7
    dp = [[0] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = 1
    for i in range(x + 1):
        for j in range(y + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j - 2] % mod
            if j > 0:
                dp[i][j] += dp[i - 2][j - 1] % mod
    return dp[x][y] % mod
x, y = map(int, input().split())
print(knight(x, y))
