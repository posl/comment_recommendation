def main():
    N = int(input())
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    for i in range(1,N+1):
        dp[i] = dp[i//2] + dp[i//3]
    print(dp[N])
