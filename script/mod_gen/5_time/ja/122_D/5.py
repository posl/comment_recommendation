def count_case(N):
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = 4 * dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
        if i >= 3:
            dp[i] += dp[i - 3]
        if i >= 4:
            dp[i] += dp[i - 4]
        dp[i] %= MOD
    return dp[N]
N = int(input())
print(count_case(N))
