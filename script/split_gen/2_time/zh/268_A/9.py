def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[-float("inf")]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            if j == 0:
                dp[i+1][j] = 0
            else:
                dp[i+1][j] = max(dp[i][j],dp[i][j-1]+j*a[i])
    print(max(dp[n]))
