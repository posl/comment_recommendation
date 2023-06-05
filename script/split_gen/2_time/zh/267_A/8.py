def get_max_size():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))
    snuke.sort(key=lambda x: x[0])
    # print(snuke)
    # dp = [[0 for i in range(5)] for j in range(n)]
    dp = [[0 for i in range(5)] for j in range(2)]
    for i in range(n):
        for j in range(5):
            if j == snuke[i][1]:
                dp[1][j] = max(dp[0][j], dp[0][j - 1], dp[0][j + 1]) + snuke[i][2]
            else:
                dp[1][j] = max(dp[0][j], dp[0][j - 1], dp[0][j + 1])
        dp[0] = dp[1]
    return max(dp[1])
