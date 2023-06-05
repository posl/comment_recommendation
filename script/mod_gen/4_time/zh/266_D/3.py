def solve():
    n = int(input())
    x = [0] * (n+1)
    t = [0] * (n+1)
    a = [0] * (n+1)
    for i in range(1, n+1):
        t[i], x[i], a[i] = map(int, input().split())
    dp = [[0]*5 for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(5):
            dp[i][j] = dp[i-1][j]
        if x[i] == 0:
            dp[i][0] = max(dp[i][0], dp[i-1][0] + a[i])
        elif x[i] == 1:
            dp[i][1] = max(dp[i][1], dp[i-1][0] + a[i])
            dp[i][0] = max(dp[i][0], dp[i-1][1] + a[i])
        elif x[i] == 2:
            dp[i][2] = max(dp[i][2], dp[i-1][1] + a[i])
            dp[i][1] = max(dp[i][1], dp[i-1][2] + a[i])
        elif x[i] == 3:
            dp[i][3] = max(dp[i][3], dp[i-1][2] + a[i])
            dp[i][2] = max(dp[i][2], dp[i-1][3] + a[i])
        elif x[i] == 4:
            dp[i][4] = max(dp[i][4], dp[i-1][3] + a[i])
            dp[i][3] = max(dp[i][3], dp[i-1][4] + a[i])
    print(max(dp[n][0], dp[n][1], dp[n][2], dp[n][3], dp[n][4]))
solve()
