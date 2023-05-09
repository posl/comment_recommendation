def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: (x[1], x[0]))
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for l, r in LR:
            if i - l >= 0:
                dp[i + r] += dp[i - l]
                dp[i + r] %= 998244353
    print(dp[-1])
