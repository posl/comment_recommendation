def main():
    S = input()
    N = len(S)
    dp = [[0 for i in range(13)] for j in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(10):
            if S[i] == '?':
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
            else:
                j = int(S[i])
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
        for j in range(13):
            dp[i+1][j] %= 10**9+7
    print(dp[N][5])

if __name__ == '__main__':
    main()