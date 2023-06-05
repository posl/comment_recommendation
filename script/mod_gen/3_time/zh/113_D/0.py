def amidakuji(h, w, k):
    # 初始化
    # dp[i][j]：第i列，第j行的走法
    dp = [[0 for i in range(h+1)] for j in range(w+1)]
    # 1列，1行的走法
    dp[1][1] = 1
    # 递推
    for i in range(2, w+1):
        for j in range(1, h+1):
            # 从上一列的下一行走到当前列的当前行
            dp[i][j] += dp[i-1][j+1]
            # 从上一列的上一行走到当前列的当前行
            dp[i][j] += dp[i-1][j-1]
    return dp[k][1] % 1000000007
h, w, k = map(int, input().split())
print(amidakuji(h, w, k))
