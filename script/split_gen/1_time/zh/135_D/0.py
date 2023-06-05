def main():
    S = input()
    mod = 10**9+7
    dp = [[0]*13 for _ in range(len(S)+1)]
    dp[0][0] = 1
    for i in range(len(S)):
        for j in range(10):
            if S[i] == '?':
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
            else:
                dp[i+1][(int(S[i])*10+j)%13] += dp[i][j]
        for k in range(13):
            dp[i+1][k] %= mod
    print(dp[len(S)][5])
