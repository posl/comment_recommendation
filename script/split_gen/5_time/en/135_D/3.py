def solve():
    s = input()
    mod = 10**9 + 7
    dp = [[0 for _ in range(13)] for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i in range(len(s)):
        if s[i] == "?":
            for j in range(10):
                for k in range(13):
                    dp[i+1][(j*10+k)%13] += dp[i][k]
        else:
            for k in range(13):
                dp[i+1][(int(s[i])*10+k)%13] += dp[i][k]
        for k in range(13):
            dp[i+1][k] %= mod
    print(dp[-1][5])
