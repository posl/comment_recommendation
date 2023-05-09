def main():
    N, K = map(int, input().split())
    L = []
    R = []
    for i in range(K):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    mod = 998244353
    dp = [0 for _ in range(N)]
    dp[0] = 1
    for i in range(1, N):
        for j in range(K):
            if i - L[j] >= 0:
                dp[i] += dp[i - L[j]]
                dp[i] %= mod
            if i - R[j] - 1 >= 0:
                dp[i] -= dp[i - R[j] - 1]
                dp[i] %= mod
    print(dp[N - 1])

if __name__ == '__main__':
    main()