def main():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    # dp[i] = マスiに行く方法の個数
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l, r = LR[j]
            li = i - r
            ri = i - l
            if ri < 0:
                continue
            li = max(li, 1)
            dp[i] += dpsum[ri] - dpsum[li - 1]
        dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])
