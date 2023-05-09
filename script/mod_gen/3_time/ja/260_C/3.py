def solve():
    #n, x, y = map(int, input().split())
    n, x, y = 10, 5, 5
    dp = [0] * (n+1)
    dp[2] = min(x, y) + 1
    for i in range(3, n+1):
        dp[i] = min(dp[i-1] + x, dp[i-2] + y) + 1
    print(dp[n])

if __name__ == '__main__':
    solve()