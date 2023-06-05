def solve(n, x, bags):
    # 判断是否有解
    if x == 1:
        return 1
    # 由于每个袋子里面的球都是不同的，所以可以把袋子里面的球看成是相同的。
    # 所以可以把问题转化成从n个球中选出一个球，使得这个球上的数字的乘积为x。
    # 那么可以用动态规划来解决这个问题。
    # dp[i][j]表示从前i个球中选出一个球，使得这个球上的数字的乘积为j的方案数。
    # dp[i][j] = dp[i-1][j//balls[i]] + dp[i-1][j]。
    # 其中balls[i]表示第i个球上的数字。
    # 由于j//balls[i]和j都是小于j的，所以可以只用一维数组来表示dp数组。
    # dp[j] = dp[j//balls[i]] + dp[j]
    # 由于dp[j//balls[i]]和dp[j]都是在第i-1次循环中得到的值，所以可以从后往前遍历。
    # dp[j] = dp[j] + dp[j//balls[i]]
    # 由于dp[j//balls[i]]和dp[j]都是在第i次循环中得到的值，所以可以从前往后遍历。
    # dp[j] = dp[j] + dp[j//balls[i]]
    # 由于dp[j//balls[i]]和dp[j]都是在第i次循环中得到的值，所以可以从前往后遍历。
    # dp[j] = dp[j] + dp[j//balls[i]]
    # 由于dp[j//balls[i]]和dp[j]都是在第i次循环中得到的值，所以可以从前往后遍历。
    # dp[j] = dp[j] + dp[j//balls[i]]
    # 由于dp[j//balls

if __name__ == '__main__':
    solve()