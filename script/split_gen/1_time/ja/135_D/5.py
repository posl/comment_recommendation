def solve():
    S = input()
    N = len(S)
    dp = [[0 for i in range(13)] for j in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(13):
            if S[i] != "?":
                dp[i+1][(j*10+int(S[i]))%13] += dp[i][j]
            else:
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
        for j in range(13):
            dp[i+1][j] %= 10**9+7
    print(dp[N][5])
