def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c_,y_ = map(int,input().split())
        c.append(c_)
        y.append(y_)
    dp = [[-1 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                continue
            #表が出た場合
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+x[i])
            #裏が出た場合
            dp[i+1][0] = max(dp[i+1][0],dp[i][j])
            #ボーナスの処理
            for k in range(m):
                if j+1 == c[k]:
                    dp[i+1][0] = max(dp[i+1][0],dp[i][j]+y[k])
    ans = 0
    for i in range(n+1):
        ans = max(ans,dp[n][i])
    print(ans)
