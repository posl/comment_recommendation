def main():
    n,m = list(map(int,input().split()))
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_i, y_i = list(map(int,input().split()))
        c.append(c_i)
        y.append(y_i)
    #print(n,m,x,c,y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,n+1):
        dp[0][i] = dp[0][i-1] + x[i-1]
    #print(dp)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if j < c[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-c[i-1]]+y[i-1])
    #print(dp)
    print(dp[-1][-1])
