def main():
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]
    mod = 998244353
    dp = [0] * (n+1)
    dp[1] = 1
    dpsum = [0] * (n+1)
    dpsum[1] = 1
    for i in range(2, n+1):
        for l, r in lr:
            if i-l < 1:
                continue
            dp[i] += dpsum[i-l] - dpsum[max(0, i-r-1)]
            dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod
    print(dp[n])
