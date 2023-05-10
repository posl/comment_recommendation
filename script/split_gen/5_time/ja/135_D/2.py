def solve():
    s = input()
    n = len(s)
    dp = [[0]*13 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(10):
            if s[i] != '?' and s[i] != str(j): continue
            for k in range(13):
                dp[i+1][(k*10+j)%13] += dp[i][k]
                dp[i+1][(k*10+j)%13] %= 10**9+7
    print(dp[n][5])
solve()
