def solve(n, a, b, s):
    # dp[i][j] = min cost to make s[i:j+1] a palindrome
    # dp[i][j] = min(dp[i+1][j] + a, dp[i][j-1] + a, dp[i+1][j-1] + b if s[i] != s[j])
    dp = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n - j):
            if i == j + i:
                continue
            if s[i] == s[j + i]:
                dp[i][j + i] = dp[i + 1][j + i - 1]
            else:
                dp[i][j + i] = min(dp[i + 1][j + i] + a, dp[i][j + i - 1] + a, dp[i + 1][j + i - 1] + b)
    return dp[0][n - 1]
n, a, b = map(int, input().split())
s = input()
print(solve(n, a, b, s))
