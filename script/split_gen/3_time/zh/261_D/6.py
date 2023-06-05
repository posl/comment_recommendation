def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    c = []
    y = []
    for i in range(m):
        c1,y1 = map(int,input().split())
        c.append(c1)
        y.append(y1)
    dp = [[-1 for i in range(n+1)] for j in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            if dp[i][j] >= 0:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                if j+1 <= n:
                    dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] + x[i])
    ans = 0
    for i in range(n+1):
        for j in range(n+1):
            if dp[i][j] >= 0:
                for k in range(m):
                    if j >= c[k]:
                        dp[i][j-c[k]] = max(dp[i][j-c[k]],dp[i][j] + y[k])
                    ans = max(ans,dp[i][j])
    print(ans)
