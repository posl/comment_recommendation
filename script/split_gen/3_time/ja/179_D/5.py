def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(1, N+1):
        for l, r in LR:
            if i+l <= N:
                dp[i+l] += dp[i]
                dp[i+l] %= mod
            if i+r+1 <= N:
                dp[i+r+1] -= dp[i]
                dp[i+r+1] %= mod
        dp[i] += dp[i-1]
        dp[i] %= mod
    print(dp[N])
