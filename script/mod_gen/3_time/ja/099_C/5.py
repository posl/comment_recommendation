def solve(n):
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for i in range(n+1):
        for j in range(1, 100):
            if i + 6**j <= n:
                dp[i+6**j] = min(dp[i+6**j], dp[i]+1)
            if i + 9**j <= n:
                dp[i+9**j] = min(dp[i+9**j], dp[i]+1)
    print(dp[n])
    return

if __name__ == '__main__':
    solve()