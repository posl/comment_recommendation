def climbStairs(n, m, a):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            if i in a:
                dp[i] = 0
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
print(climbStairs(n, m, a) % (10**9+7))
