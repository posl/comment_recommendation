def main():
    h, w, k = map(int, input().split())
    dp = [0] * (w + 2)
    dp[1] = 1
    mod = 1000000007
    for i in range(h):
        ndp = [0] * (w + 2)
        for j in range(1, w + 1):
            ndp[j] = dp[j - 1] * dp[j] % mod + dp[j + 1] * dp[j] % mod
            ndp[j] %= mod
        dp = ndp
    print(dp[k])
