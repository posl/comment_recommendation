def getNumOfIntAvg(nums):
    n = len(nums)
    # dp[i][j]表示前i个数中，选出j个数，这些数的和为i的情况数
    dp = [[0 for i in range(n+1)] for j in range(sum(nums)+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(sum(nums)+1):
            dp[j][i+1] += dp[j][i]
            if j >= nums[i]:
                dp[j][i+1] += dp[j-nums[i]][i]
    res = 0
    for i in range(1, sum(nums)+1):
        if i % n == 0:
            res += dp[i][n]
    return res
