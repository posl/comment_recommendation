def main():
    S = input()
    mod = 10**9 + 7
    n = len(S)
    dp = [[0]*13 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(13):
            if S[i] == '?':
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
                    dp[i+1][(j*10+k)%13] %= mod
            else:
                dp[i+1][(j*10+int(S[i]))%13] += dp[i][j]
                dp[i+1][(j*10+int(S[i]))%13] %= mod
    print(dp[n][5])

if __name__ == '__main__':
    main()