def main():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for l, r in LR:
            li = max(0, i - r)
            ri = max(0, i - l + 1)
            dp[i] += dpsum[ri] - dpsum[li]
            dp[i] %= MOD
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= MOD
    print(dp[N])

if __name__ == '__main__':
    main()