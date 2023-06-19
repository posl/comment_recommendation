def solve(n, k):
    mod = 10 ** 9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] * j) % mod
    ans = [0] * (k + 1)
    for i in range(1, k + 1):
        ans[i] = dp[n][i] * dp[n - 1][k - i] % mod
    return ans
n, k = map(int, input().split())
print('
'.join(map(str, solve(n, k))))
