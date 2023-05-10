def solve():
    s = int(input())
    mod = 10**9 + 7
    dp = [0] * (s + 1)
    dp[0] = 1
    for i in range(3, s + 1):
        dp[i] = dp[i - 3] + dp[i - 1]
        dp[i] %= mod
    print(dp[s])
