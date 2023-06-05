def solve(n, m, k):
    dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        for j in range(m + 1):
            for s in range(k + 1):
                dp[i][j][s] += dp[i - 1][j][s]
                if j > 0 and s >= i:
                    dp[i][j][s] += dp[i - 1][j - 1][s - i]
                dp[i][j][s] %= 998244353
    return dp[n][m][k]
n, m, k = map(int, input().split())
print(solve(n, m, k))
