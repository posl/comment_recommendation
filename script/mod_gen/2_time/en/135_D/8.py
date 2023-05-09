def main():
    S = input()
    N = len(S)
    # dp[i][j] = count of i-th digit and remainder j
    dp = [[0 for _ in range(13)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(13):
            if S[i-1] == '?':
                for k in range(10):
                    dp[i][(j*10+k)%13] += dp[i-1][j]
            else:
                dp[i][(j*10+int(S[i-1]))%13] += dp[i-1][j]
    print(dp[N][5]%(10**9+7))

if __name__ == '__main__':
    main()