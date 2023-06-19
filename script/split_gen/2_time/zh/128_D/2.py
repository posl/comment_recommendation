def solve(n,k,nums):
    dp = [[[-float('inf') for i in range(2)] for j in range(k+1)] for k in range(n+1)]
    dp[0][0][0] = 0
    dp[0][0][1] = 0
    for i in range(n):
        for j in range(k+1):
            dp[i+1][j][0] = max(dp[i+1][j][0],dp[i][j][0])
            dp[i+1][j][1] = max(dp[i+1][j][1],dp[i][j][1])
            if j < k:
                dp[i+1][j+1][1] = max(dp[i+1][j+1][1],dp[i][j][0]+nums[i])
                dp[i+1][j+1][0] = max(dp[i+1][j+1][0],dp[i][j][1]-nums[i])
    return max(dp[n][k][0],dp[n][k][1])
n,k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
print(solve(n,k,nums))
