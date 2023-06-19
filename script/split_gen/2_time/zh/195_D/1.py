def get_max_value(w, v, x):
    # w: weight
    # v: value
    # x: box size
    # return: max value
    dp = [[0 for _ in range(10001)] for _ in range(51)]
    for i in range(1, len(w)+1):
        for j in range(1, 10001):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
    # print(dp)
    return dp[len(w)][x]
