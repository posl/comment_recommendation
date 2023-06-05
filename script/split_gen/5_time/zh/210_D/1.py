def main():
    h,w,c = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    #print(h,w,c,a)
    dp = [[0 for _ in range(w)] for _ in range(h)]
    #print(dp)
    #dp[i][j]表示从（i,j）出发的最小成本
    dp[0][0] = a[0][0]
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] = min(dp[i][j-1],a[i][j]+c*(j+1))
            elif j == 0:
                dp[i][j] = min(dp[i-1][j],a[i][j]+c*(i+1))
            else:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],a[i][j]+c*(i+1+j+1))
    #print(dp)
    ans = 10**9
    for i in range(h):
        for j in range(w):
            for k in range(i,h):
                for l in range(j,w):
                    if i == k and j == l:
                        continue
                    if i == 0 and j == 0:
                        ans = min(ans,dp[k][l])
                    elif i == 0:
                        ans = min(ans,dp[k][l]-dp[k][j-1])
                    elif j == 0:
                        ans = min(ans,dp[k][l]-dp[i-1][l])
                    else:
                        ans = min(ans,dp[k][l]-dp[i-1][l]-dp[k][j-1]+dp[i-1][j-1])
    print(ans)
