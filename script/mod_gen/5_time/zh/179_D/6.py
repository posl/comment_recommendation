def main():
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    dpsum = [0] * (N+1)
    dpsum[1] = 1
    for i in range(2, N+1):
        for j in range(K):
            l = max(0, i - LR[j][1])
            r = i - LR[j][0]
            if r < 0:
                continue
            dp[i] += dpsum[r] - dpsum[l-1]
        dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
    print(dp[N])

if __name__ == '__main__':
    main()