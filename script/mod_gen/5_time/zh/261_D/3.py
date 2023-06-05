def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_,y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)
    c_y = list(zip(c,y))
    c_y.sort(key=lambda x:x[0])
    #print(c_y)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i == 0:
                if j+1 == c_y[i][0]:
                    dp[i][j+1] = max(dp[i][j],dp[i][j]+c_y[i][1])
                else:
                    dp[i][j+1] = dp[i][j]
            else:
                if j+1 == c_y[i][0]:
                    dp[i][j+1] = max(dp[i-1][j],dp[i][j],dp[i][j+1]+c_y[i][1])
                else:
                    dp[i][j+1] = dp[i][j]
    #print(dp)
    print(dp[n-1][n])

if __name__ == '__main__':
    main()