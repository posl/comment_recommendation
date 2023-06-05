def main():
    s = input()
    l = len(s)
    mod = 10**9+7
    dp = [[0]*13 for _ in range(l+1)]
    dp[0][0] = 1
    for i in range(l):
        for j in range(13):
            if s[i] == '?':
                for k in range(10):
                    dp[i+1][(j*10+k)%13] += dp[i][j]
            else:
                k = int(s[i])
                dp[i+1][(j*10+k)%13] += dp[i][j]
            dp[i+1][j] %= mod
    print(dp[l][5])
    return
