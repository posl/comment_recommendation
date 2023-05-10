def get_max_reward(n, m, x_list, c_list, y_list):
    # dp[i][j] = i回目のコイントスを終えた時点で、カウンタの数値がjである時の最大報酬
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            # i回目のコイントスで表が出た時
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+x_list[i])
            # i回目のコイントスで裏が出た時
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])
            # i回目のコイントスでボーナスが出た時
            for k in range(m):
                if j+1 == c_list[k]:
                    dp[i+1][c_list[k]] = max(dp[i+1][c_list[k]], dp[i][j]+y_list[k])
    return max(dp[-1])
