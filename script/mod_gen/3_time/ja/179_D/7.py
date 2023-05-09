def main():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * N
    dp[0] = 1
    for i in range(1, N):
        for l, r in LR:
            if i - l < 0:
                continue
            dp[i] += dp[i-l] % mod
            dp[i] -= dp[max(0, i-r-1)] % mod
        dp[i] %= mod
    print(dp[-1])

if __name__ == '__main__':
    main()