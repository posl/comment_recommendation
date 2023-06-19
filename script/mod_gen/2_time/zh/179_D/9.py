def main():
    # 读入数据
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    # 你的代码
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N + 1):
        for l, r in LR:
            if i + l <= N:
                dp[i + l] += dp[i]
                dp[i + l] %= mod
            if i + r + 1 <= N:
                dp[i + r + 1] -= dp[i]
                dp[i + r + 1] %= mod
        dp[i + 1] += dp[i]
        dp[i + 1] %= mod
    # 打印答案
    print(dp[N])

if __name__ == '__main__':
    main()