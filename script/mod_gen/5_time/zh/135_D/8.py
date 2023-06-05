def main():
    s = input()
    mod = 1000000007
    n = len(s)
    dp = [[0 for _ in range(13)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        if s[i-1] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i][(k*10+j)%13] += dp[i-1][k]
        else:
            for k in range(13):
                dp[i][(k*10+int(s[i-1]))%13] += dp[i-1][k]
        for j in range(13):
            dp[i][j] %= mod
    print(dp[n][5])

if __name__ == '__main__':
    main()