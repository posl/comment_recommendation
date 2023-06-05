def climb_stairs(n, m, a):
    # 0到n的台阶，m个破损台阶，a为破损台阶的位置
    # 状态转移方程：dp[i] = dp[i-1] + dp[i-2]
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i not in a:
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1000000007
