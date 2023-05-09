def main():
    s = input()
    l = len(s)
    dp = [[0 for _ in range(13)] for _ in range(l+1)]
    dp[0][0] = 1
    for i in range(l):
        if s[i] == '?':
            for j in range(10):
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
                    dp[i+1][(k*10+j)%13] %= 10**9+7
        else:
            for k in range(13):
                dp[i+1][(k*10+int(s[i]))%13] += dp[i][k]
                dp[i+1][(k*10+int(s[i]))%13] %= 10**9+7
    print(dp[l][5])
