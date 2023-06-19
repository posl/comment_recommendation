def solve(h, w, k):
    mod = 10**9 + 7
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    dp[0][1] = 1
    for i in range(h):
        for j in range(1, w + 1):
            if j == 1:
                dp[i + 1][j] = dp[i][j] + dp[i][j + 1]
            elif j == w:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j] + dp[i][j + 1]
    return dp[h][k] % mod
h, w, k = map(int, input().split())
print(solve(h, w, k))
