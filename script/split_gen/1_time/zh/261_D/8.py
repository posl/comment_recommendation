def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_, y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)
    #print(n,m,x,c,y)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i][j+1],dp[i][j]+x[i])
    #print(dp)
    ans = 0
    for i in range(m):
        for j in range(n+1):
            ans = max(ans,dp[j][j-c[i]]+y[i])
    print(ans)
