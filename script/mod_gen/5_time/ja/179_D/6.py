def main():
    n, k = map(int, input().split())
    lrs = [list(map(int, input().split())) for _ in range(k)]
    MOD = 998244353
    # dp[i]: マスiに到達する方法の数
    dp = [0] * (n+1)
    dp[1] = 1
    dpsum = [0] * (n+1)
    dpsum[1] = 1
    for i in range(2, n+1):
        for l, r in lrs:
            li = max(i-l, 1)
            ri = max(i-r-1, 0)
            dp[i] += dpsum[li] - dpsum[ri]
            dp[i] %= MOD
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= MOD
    print(dp[n])

if __name__ == '__main__':
    main()