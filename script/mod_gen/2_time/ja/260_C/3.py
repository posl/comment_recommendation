def solve():
    N, X, Y = map(int, input().split())
    dp = [0]*(N+1)
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + X
        for j in range(2, i):
            dp[i] = min(dp[i], dp[j-1] + X + (i-j)*Y)
    print(dp[-1])
    return 0

if __name__ == '__main__':
    solve()