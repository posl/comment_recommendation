def main():
    s = input()
    len_s = len(s)
    dp = [[0 for _ in range(13)] for _ in range(len_s+1)]
    dp[0][0] = 1
    for i in range(len_s):
        if s[i] == "?":
            for j in range(10):
                for k in range(13):
                    dp[i+1][(k*10+j)%13] += dp[i][k]
        else:
            for k in range(13):
                dp[i+1][(k*10+int(s[i]))%13] += dp[i][k]
        for k in range(13):
            dp[i+1][k] %= 10**9+7
    print(dp[len_s][5])
