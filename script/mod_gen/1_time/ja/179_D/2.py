def main():
    N, K = map(int, input().split())
    LR = []
    for _ in range(K):
        l, r = map(int, input().split())
        LR.append((l, r))
    mod = 998244353
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    S = [0] * (N + 1)
    S[0] = 1
    S[1] = 2
    for i in range(2, N + 1):
        for l, r in LR:
            dp[i] += S[max(0, i - r)] - S[max(0, i - l)]
        S[i] = S[i - 1] + dp[i]
        dp[i] %= mod
        S[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()