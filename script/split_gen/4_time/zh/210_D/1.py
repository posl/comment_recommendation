def min_cost():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for _ in range(2):
        dp = [[10**18] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
                    ans = min(ans, dp[i-1][j] + C + A[i][j] + C)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
                    ans = min(ans, dp[i][j-1] + C + A[i][j] + C)
                dp[i][j] = min(dp[i][j], A[i][j])
    print(ans)
min_cost()
