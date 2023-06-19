def getMinDiff(arr, n):    
    sum = 0
    for i in arr:
        sum += i
    dp = [[False for i in range(sum + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, sum + 1):
        dp[0][i] = False
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]
    diff = 1000000007
    for j in range(sum // 2, -1, -1):
        if dp[n][j] == True:
            diff = sum - 2 * j
            break
    return diff
n = int(input())
arr = list(map(int, input().split()))
print(getMinDiff(arr, n))
