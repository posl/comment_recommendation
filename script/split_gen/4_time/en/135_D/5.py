def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[0]*13 for i in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        c = S[i]
        for j in range(13):
            if c == "?":
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
            else:
                k = int(c)
                dp[i+1][(j*10+k)%13] += dp[i][j]
            dp[i+1][(j*10+k)%13] %= MOD
    print(dp[N][5])
