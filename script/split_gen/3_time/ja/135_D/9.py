def main():
    s = input()
    n = len(s)
    # dp[i][j] := 上からi桁目まで見て、13で割った余りがjであるような数の個数
    dp = [[0]*13 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(13):
            if s[i] == '?':
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
                    dp[i+1][(j*10+k)%13] %= 10**9+7
            else:
                dp[i+1][(j*10+int(s[i]))%13] += dp[i][j]
                dp[i+1][(j*10+int(s[i]))%13] %= 10**9+7
    print(dp[n][5])
