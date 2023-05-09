def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] * 10 % MOD
    ans = dp[N] - (dp[N // 2] + dp[(N + 1) // 2]) % MOD
    if ans < 0:
        ans += MOD
    print(ans)
