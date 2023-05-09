def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    MOD = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    cum = [0] * (N + 1)
    cum[1] = 1
    for i in range(2, N + 1):
        for l, r in LR:
            dp[i] += cum[max(0, i - r - 1)] - cum[max(0, i - l)]
            dp[i] %= MOD
        cum[i] = cum[i - 1] + dp[i]
    print(dp[N])

if __name__ == '__main__':
    main()