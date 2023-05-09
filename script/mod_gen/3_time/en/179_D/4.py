def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    LR.sort(key=lambda x: x[0])
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for l, r in LR:
            dp[i + l] += dp[i]
            dp[i + l] %= 998244353
            dp[i + r + 1] -= dp[i]
            dp[i + r + 1] %= 998244353
    print(dp[N])

if __name__ == '__main__':
    main()