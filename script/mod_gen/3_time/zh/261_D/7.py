def main():
    # 读入数据
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_,y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)
    # 初始化
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    # 递推
    for i in range(1,n+1):
        dp[0][i] = dp[0][i-1] + x[i-1]
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if j >= c[i-1]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-c[i-1]]+y[i-1])
    # 输出
    print(dp[m][n])

if __name__ == '__main__':
    main()