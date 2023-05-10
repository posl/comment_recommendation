def solve(h, w, k):
    if w == 1:
        return 1
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    dp[0][1] = 1
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            dp[i][j] = dp[i - 1][j - 1] * dp[i - 1][j] + dp[i - 1][j] * dp[i - 1][j + 1]
    return dp[h][k] % 1000000007
h, w, k = map(int, input().split())
print(solve(h, w, k))
