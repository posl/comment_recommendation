def get_result(n, a, b):
    # 1. 每个任务的最优解
    # 2. 两个任务的最优解
    # 3. 三个任务的最优解
    # 4. ...
    # 每个任务的最优解 = min(完成任务A的时间，完成任务B的时间)
    # 两个任务的最优解 = min(完成任务A的时间，完成任务B的时间)，两个任务分配给同一个人
    # 三个任务的最优解 = min(完成任务A的时间，完成任务B的时间)，三个任务分配给同一个人
    # ...
    # 这样的话，我们就可以得到一个动态规划的解法
    # dp[i] = min(dp[i-1] + a[i], dp[i-2] + b[i])
    # dp[0] = a[0], dp[1] = min(a[0] + a[1], b[0])
    # dp[i]表示前i个任务的最优解
    # dp[i-1] + a[i]表示第i个任务分配给一个人，前i-1个任务分配给另一个人
    # dp[i-2] + b[i]表示第i个任务分配给另一个人，前i-2个任务分配给另一个人
    dp = [0 for i in range(n)]
    dp[0] = a[0]
    dp[1] = min(a[0] + a[1], b[0])
    for i in range(2, n):
        dp[i] = min(dp[i-1] + a[i], dp[i-2] + b[i-1])
    return dp[n-1]
n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(get_result(n, a, b))
