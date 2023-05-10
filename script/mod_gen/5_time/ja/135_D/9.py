def solve():
    s = input()
    n = len(s)
    dp = [[0]*13 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        if s[i] == '?':
            for k in range(10):
                for j in range(13):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
        else:
            for j in range(13):
                dp[i+1][(j*10+int(s[i]))%13] += dp[i][j]
        for j in range(13):
            dp[i+1][j] %= 10**9+7
    print(dp[n][5])
solve()

if __name__ == '__main__':
    solve()