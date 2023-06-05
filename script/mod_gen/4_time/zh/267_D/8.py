def main():
    # input
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    # process
    # dp[i][j] 表示前i个数中选出j个数的最大值
    dp = [[-10**10 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            if j+1<=m:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+a[i]*(j+1))
    # output
    print(max(dp[n]))

if __name__ == '__main__':
    main()