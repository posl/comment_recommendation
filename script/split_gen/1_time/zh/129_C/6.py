def climb_stairs(n, m, a):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        if i in a:
            dp[i] = 0
        else:
            if i == 1:
                dp[i] = dp[i-1]
            else:
                dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]
n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(int(input()))
print(climb_stairs(n, m, a))
