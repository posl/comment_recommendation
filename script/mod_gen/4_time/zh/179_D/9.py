def main():
    N, K = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(K)]
    mod = 998244353
    dp = [0] * (N+1)
    dp[1] = 1
    for i in range(2, N+1):
        for l, r in LRs:
            if i-l >= 0:
                dp[i] += dp[i-l]
                dp[i] %= mod
            if i-r-1 >= 0:
                dp[i] -= dp[i-r-1]
                dp[i] %= mod
    print(dp[N])

if __name__ == '__main__':
    main()