def main():
    n, k = map(int, input().split())
    lrs = [tuple(map(int, input().split())) for _ in range(k)]
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for l, r in lrs:
            dp[i] += dp[i - l] - dp[i - r - 1]
    print((dp[n] % 998244353 + 998244353) % 998244353)
