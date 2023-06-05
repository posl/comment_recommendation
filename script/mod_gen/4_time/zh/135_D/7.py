def solve():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    dp = [[0 for i in range(13)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(13):
            for k in range(10):
                if s[i] != '?' and int(s[i]) != k:
                    continue
                dp[i+1][(j*10+k)%13] += dp[i][j]
                dp[i+1][(j*10+k)%13] %= mod
    print(dp[n][5])

if __name__ == '__main__':
    solve()