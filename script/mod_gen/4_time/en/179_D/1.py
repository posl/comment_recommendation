def main():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for l, r in LRs:
            if i - l < 1:
                continue
            dp[i] += dpsum[i - l] - dpsum[max(0, i - r - 1)]
            dp[i] %= mod
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()