def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * N
    dp[0] = 1
    for i in range(N):
        for l, r in LR:
            if i + l < N:
                dp[i + l] += dp[i]
                dp[i + l] %= MOD
            if i + r + 1 < N:
                dp[i + r + 1] -= dp[i]
                dp[i + r + 1] %= MOD
    for i in range(1, N):
        dp[i] += dp[i - 1]
        dp[i] %= MOD
    print(dp[N - 1])
