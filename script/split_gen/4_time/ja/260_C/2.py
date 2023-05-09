def solve():
    #n, x, y = map(int, input().split())
    n, x, y = 10, 5, 5
    #n, x, y = 2, 3, 4
    #dp = [0] * (n + 1)
    #dp[1] = 1
    #for i in range(2, n + 1):
    #    dp[i] = min(dp[i - 1] + x, dp[i // 2] + y) if i % 2 == 0 else dp[i - 1] + x
    #print(dp[n])
    #dp = [0] * (n + 1)
    #dp[1] = 1
    #for i in range(2, n + 1):
    #    dp[i] = dp[i - 1] + x
    #    if i % 2 == 0:
    #        dp[i] = min(dp[i], dp[i // 2] + y)
    #print(dp[n])
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n):
        dp[i + 1] = min(dp[i + 1], dp[i] + x)
        if i * 2 <= n:
            dp[i * 2] = min(dp[i * 2], dp[i] + y)
    print(dp[n])
