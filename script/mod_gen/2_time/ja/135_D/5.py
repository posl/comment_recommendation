def main():
    S = input()
    mod = 10**9+7
    dp = [[0]*13 for _ in range(len(S)+1)]
    dp[0][0] = 1
    for i in range(len(S)):
        if S[i] != "?":
            for j in range(13):
                dp[i+1][(j*10+int(S[i]))%13] += dp[i][j]
                dp[i+1][(j*10+int(S[i]))%13] %= mod
        else:
            for j in range(13):
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
                    dp[i+1][(j*10+k)%13] %= mod
    print(dp[len(S)][5])

if __name__ == '__main__':
    main()