def problem():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    # print(a)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + a[i] * (j+1))
    # for i in range(n+1):
    #     print(dp[i])
    print(dp[n][m])
