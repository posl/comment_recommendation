def main():
    mod = 10**9+7
    s = input()
    n = len(s)
    dp = [[0]*13 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        c = s[i]
        for j in range(13):
            if c == "?":
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
                    dp[i+1][(j*10+k)%13] %= mod
            else:
                dp[i+1][(j*10+int(c))%13] += dp[i][j]
                dp[i+1][(j*10+int(c))%13] %= mod
    print(dp[n][5])
