def max_value(n, k, v):
    #dp[i][j][0] = i回操作して、j個残っているときに、左端をとったときの最大価値
    #dp[i][j][1] = i回操作して、j個残っているときに、右端をとったときの最大価値
    dp = [[[0 for _ in range(2)] for _ in range(n+1)] for _ in range(k+1)]
    for i in range(k):
        for j in range(n+1):
            if j == 0:
                dp[i+1][j][0] = dp[i][j][0]
                dp[i+1][j][1] = dp[i][j][1]
            else:
                dp[i+1][j][0] = max(dp[i][j][0]+v[j-1], dp[i][j][0])
                dp[i+1][j][1] = max(dp[i][j][1]+v[n-j], dp[i][j][1])
                if i > 0:
                    dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j-1][1]+v[j-1])
                    dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j-1][0]+v[n-j])
    return max(dp[k][n][0], dp[k][n][1])
n, k = map(int, input().split())
v = list(map(int, input().split()))
print(max_value(n, k, v))
