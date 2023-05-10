def solve():
    N = int(input())
    dp = [float('inf')] * (N+1)
    dp[0] = 0
    for i in range(1,N+1):
        dp[i] = min(dp[i], dp[i-1]+1)
        j = 6
        while i-j >= 0:
            dp[i] = min(dp[i], dp[i-j]+1)
            j *= 6
        j = 9
        while i-j >= 0:
            dp[i] = min(dp[i], dp[i-j]+1)
            j *= 9
    print(dp[N])

if __name__ == '__main__':
    solve()