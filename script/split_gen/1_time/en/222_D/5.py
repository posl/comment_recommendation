def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = (dp[i - 1] * (B[i - 1] - A[i - 1] + 1)) % MOD
        if i >= 2:
            dp[i] += (dp[i - 2] * (B[i - 1] - A[i - 1] + 1) * (B[i - 2] - A[i - 2] + 1)) % MOD
            dp[i] %= MOD
    print(dp[N])
