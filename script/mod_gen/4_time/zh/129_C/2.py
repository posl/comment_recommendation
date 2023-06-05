def climb_stairs(n, m, a):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    broken = [False for i in range(n + 1)]
    for i in a:
        broken[i] = True
    for i in range(1, n + 1):
        if not broken[i]:
            if i == 1:
                dp[i] = dp[i - 1]
            else:
                dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n]

if __name__ == '__main__':
    climb_stairs()