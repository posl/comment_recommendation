def main():
    N = int(input())
    dp = [10**5]*(N+1)
    dp[0] = 0
    for n in range(1,N+1):
        for i in range(1,6):
            if n-6**i >= 0:
                dp[n] = min(dp[n],dp[n-6**i]+1)
            if n-9**i >= 0:
                dp[n] = min(dp[n],dp[n-9**i]+1)
    print(dp[N])
