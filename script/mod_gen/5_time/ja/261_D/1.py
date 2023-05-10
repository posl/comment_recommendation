def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    y = []
    for i in range(m):
        c,yy = map(int,input().split())
        y.append([c,yy])
    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = max(dp[i+1],dp[i]+x[i])
        for j in range(m):
            if i+1 >= y[j][0]:
                dp[i+1] = max(dp[i+1],dp[i+1-y[j][0]]+y[j][1])
    print(dp[n])

if __name__ == '__main__':
    main()