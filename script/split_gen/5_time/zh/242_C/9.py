def solve(n):
    dp = [[0] * 10 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(10):
            for k in range(j - 1, j + 2):
                if 0 <= k <= 9:
                    dp[i + 1][k] += dp[i][j]
    return sum(dp[n])
n = int(input())
print(solve(n) % 998244353)
