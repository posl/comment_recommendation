def solve(s,t):
    n = len(s)
    m = len(t)
    dp = [[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=dp[i-1][j]
    return m-dp[n][m]
s = input()
t = input()
print(solve(s,t))
