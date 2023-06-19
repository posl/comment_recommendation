def solve():
    S = input()
    MOD = 10**9+7
    dp = [[0]*13 for _ in range(len(S)+1)]
    dp[0][0] = 1
    for i, s in enumerate(S):
        for j in range(13):
            if s == '?':
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
            else:
                dp[i+1][(j*10+int(s))%13] += dp[i][j]
            dp[i+1][(j*10)%13] %= MOD
    print(dp[len(S)][5])
solve()
