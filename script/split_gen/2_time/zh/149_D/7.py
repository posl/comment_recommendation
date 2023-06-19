def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    # dp[i][j] = i回目までにjを選んだときの最大得点
    dp = [[0 for i in range(3)] for j in range(N+1)]
    for i in range(N):
        # 今回の手
        t = T[i]
        # 前回の手
        if i-K >= 0:
            prev = T[i-K]
        else:
            prev = "x"
        if t == "r":
            dp[i+1][0] = max(dp[i+1][0], dp[i][1] + P, dp[i][2] + P)
            if prev != "r":
                dp[i+1][0] = max(dp[i+1][0], dp[i][0] + R)
        elif t == "s":
            dp[i+1][1] = max(dp[i+1][1], dp[i][0] + R, dp[i][2] + R)
            if prev != "s":
                dp[i+1][1] = max(dp[i+1][1], dp[i][1] + S)
        elif t == "p":
            dp[i+1][2] = max(dp[i+1][2], dp[i][0] + S, dp[i][1] + S)
            if prev != "p":
                dp[i+1][2] = max(dp[i+1][2], dp[i][2] + P)
    print(max(dp[N]))
