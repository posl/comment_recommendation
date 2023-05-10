def solve(s):
    chokudai = 'chokudai'
    n = len(s)
    m = len(chokudai)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == chokudai[j-1]:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % (10**9 + 7)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][m]

if __name__ == '__main__':
    solve()