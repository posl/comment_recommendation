def main():
    S = input()
    MOD = 10**9 + 7
    dp = [[0]*13 for _ in range(len(S)+1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(13):
            if S[i] == '?':
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
            else:
                dp[i+1][(j*10+int(S[i]))%13] += dp[i][j]
            dp[i+1][(j*10)%13] %= MOD
    print(dp[len(S)][5])
