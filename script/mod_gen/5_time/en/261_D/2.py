def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_,y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)
    #print(n,m,x,c,y)
    dp = [[0]*(n+1) for i in range(n+1)]
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                dp[i][j] = -1
    #print(dp)
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                continue
            if i == j:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                dp[i+1][i+1] = max(dp[i+1][i+1],dp[i][j]+x[i])
            else:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                dp[i+1][i+1] = max(dp[i+1][i+1],dp[i][j]+x[i])
                if dp[i][j] >= c[j]:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][j]+y[j])
    #print(dp)
    ans = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                continue
            ans = max(ans,dp[i][j])
    print(ans)

if __name__ == '__main__':
    main()