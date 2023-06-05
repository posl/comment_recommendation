def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dp_sum = [0] * (N + 1)
    dp_sum[1] = 1
    for i in range(2, N + 1):
        for l, r in LR:
            li = max(i - r, 0)
            ri = i - l
            if ri < 0:
                continue
            dp[i] += dp_sum[ri] - dp_sum[li - 1]
            dp[i] %= mod
        dp_sum[i] = dp_sum[i - 1] + dp[i]
        dp_sum[i] %= mod
    print(dp[N])
