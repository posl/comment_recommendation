def main():
    n = int(input())
    mod = 10**9 + 7
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] * 10 + 1) % mod
    print((dp[n] * 2 - 1) % mod)
