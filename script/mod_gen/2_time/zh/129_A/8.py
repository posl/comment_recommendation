def solve(n, k, v):
    result = 0
    for i in range(min(n, k) + 1):
        for j in range(min(n, k) + 1 - i):
            l = max(0, i - n)
            r = max(0, j - n)
            dp = [[0] * (n + l + r + 1) for _ in range(n + 1)]
            for x in range(n + 1):
                for y in range(n + l + r + 1):
                    dp[x][y] = -float('inf')
                dp[x][0] = 0
            for x in range(n):
                for y in range(n + l + r + 1):
                    dp[x + 1][y] = max(dp[x + 1][y], dp[x][y])
                    if y + 1 < n + l + r + 1:
                        dp[x + 1][y + 1] = max(dp[x + 1][y + 1], dp[x][y] + v[x])
            result = max(result, dp[n][i + j + l])
    print(result)
    return result

if __name__ == '__main__':
    solve()