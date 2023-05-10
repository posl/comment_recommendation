def main():
    N, K = map(int, input().split())
    Ls = []
    Rs = []
    for i in range(K):
        L, R = map(int, input().split())
        Ls.append(L)
        Rs.append(R)
    dp = [0] * (N + 1)
    dp[1] = 1
    dpsum = [0] * (N + 1)
    dpsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            l = max(0, i - Rs[j])
            r = max(0, i - Ls[j] + 1)
            dp[i] += dpsum[r] - dpsum[l]
        dpsum[i] = dpsum[i - 1] + dp[i]
        dp[i] %= 998244353
        dpsum[i] %= 998244353
    print(dp[N])

if __name__ == '__main__':
    main()