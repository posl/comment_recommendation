def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(1, N):
        for j in range(K):
            l, r = LR[j]
            dp[i + l] = (dp[i + l] + dp[i]) % mod
            dp[i + r + 1] = (dp[i + r + 1] - dp[i]) % mod
    for i in range(1, N + 1):
        dp[i] = (dp[i] + dp[i - 1]) % mod
    print(dp[N])

if __name__ == '__main__':
    main()