def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    dp = [[0 for _ in range(3)] for _ in range(n+1)]
    for i in range(1,n+1):
        if t[i-1] == 'r':
            dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + p
            dp[i][1] = max(dp[i-1][0],dp[i-1][2])
            dp[i][2] = max(dp[i-1][0],dp[i-1][1])
        elif t[i-1] == 's':
            dp[i][0] = max(dp[i-1][1],dp[i-1][2])
            dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + r
            dp[i][2] = max(dp[i-1][0],dp[i-1][1])
        else:
            dp[i][0] = max(dp[i-1][1],dp[i-1][2])
            dp[i][1] = max(dp[i-1][0],dp[i-1][2])
            dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + s
        if i >= k:
            for j in range(3):
                dp[i][j] = max(dp[i][j],dp[i-k][j])
    ans = 0
    for i in range(n+1):
        for j in range(3):
            ans = max(ans,dp[i][j])
    print(ans)
