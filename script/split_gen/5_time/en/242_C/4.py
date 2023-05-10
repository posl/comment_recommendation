def main():
    N = int(input())
    dp = [0] * (N+1)
    dp[1] = 9
    dp[2] = 17
    for i in range(3, N+1):
        dp[i] = (dp[i-1] * 10 - dp[i-2]) % 998244353
    print(dp[N])
