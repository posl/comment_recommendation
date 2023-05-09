def main():
    S = input()
    MOD = 10**9+7
    n = len(S)
    dp = [[0]*13 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        if S[i] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
                    dp[i+1][(k*10+j)%13] %= MOD
        else:
            for k in range(13):
                dp[i+1][(k*10+int(S[i]))%13] += dp[i][k]
                dp[i+1][(k*10+int(S[i]))%13] %= MOD
    print(dp[n][5])
main()

if __name__ == '__main__':
    main()