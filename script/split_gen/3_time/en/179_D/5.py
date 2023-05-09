def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort()
    mod = 998244353
    dp = [0] * N
    dp[0] = 1
    for i in range(N - 1):
        for j in range(K):
            if LR[j][0] + i >= N:
                break
            dp[i + LR[j][0]] += dp[i]
            if LR[j][1] + i + 1 < N:
                dp[i + LR[j][1] + 1] -= dp[i]
            dp[i + LR[j][0]] %= mod
    for i in range(1, N):
        dp[i] += dp[i - 1]
        dp[i] %= mod
    print(dp[N - 1])
