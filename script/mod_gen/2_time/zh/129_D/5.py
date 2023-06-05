def climb_stairs(N, M, broken):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        if i in broken:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N] % 1000000007

if __name__ == '__main__':
    climb_stairs()