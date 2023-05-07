def main():
    N, K = map(int, input().split())
    L, R = [], []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        for j in range(K):
            dp[i] += dp[i - L[j]]
            dp[i] %= 998244353
            dp[i] += dp[i - R[j] - 1]
            dp[i] %= 998244353
    print(dp[N])

if __name__ == '__main__':
    main()