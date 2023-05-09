def main():
    n, k = map(int, input().split())
    mod = 998244353
    S = set()
    for _ in range(k):
        l, r = map(int, input().split())
        S |= set(range(l, r + 1))
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(1, n):
        if i in S:
            for j in range(1, n + 1):
                if i + j > n:
                    break
                dp[i + j] += dp[i]
                dp[i + j] %= mod
    print(dp[n])
