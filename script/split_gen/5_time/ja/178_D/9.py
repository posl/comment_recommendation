def main():
    n = int(input())
    mod = 10**9 + 7
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(n+1):
        for j in range(3, n+1):
            if i + j <= n:
                dp[i+j] += dp[i]
                dp[i+j] %= mod
    print(dp[n])
