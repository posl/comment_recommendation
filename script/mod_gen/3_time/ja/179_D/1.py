def main():
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l = max(0, i - R[j])
            r = max(0, i - L[j] + 1)
            dp[i] += dp[l] - dp[r]
        dp[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()