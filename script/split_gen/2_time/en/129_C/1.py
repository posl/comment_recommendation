def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    MOD = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1, N+1):
        if i not in A:
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
    print(dp[N])
