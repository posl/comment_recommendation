def main():
    s = input()
    n = len(s)
    mod = 10**9+7
    dp = [[0 for _ in range(13)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(13):
            if s[i-1] == '?':
                for k in range(10):
                    dp[i][(j*10+k)%13] += dp[i-1][j]
                    dp[i][(j*10+k)%13] %= mod
            else:
                dp[i][(j*10+int(s[i-1]))%13] += dp[i-1][j]
                dp[i][(j*10+int(s[i-1]))%13] %= mod
    print(dp[n][5])

if __name__ == '__main__':
    main()