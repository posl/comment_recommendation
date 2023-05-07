def solve(s):
    # dp[i][j] = sの最後の文字がs[i]であるときの、s[i:]についての答え
    # j = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ? のいずれか
    # j = 10は、?を0に置き換えたときの答え
    dp = [[0] * 11 for _ in range(len(s) + 1)]
    dp[len(s)][0] = 1
    for i in range(len(s) - 1, -1, -1):
        for j in range(11):
            if s[i] != '?':
                dp[i][j] += dp[i + 1][(10 * j + int(s[i])) % 13]
            else:
                for k in range(10):
                    dp[i][j] += dp[i + 1][(10 * j + k) % 13]
            dp[i][j] %= 10 ** 9 + 7
    return dp[0][5]
s = input()
print(solve(s))
