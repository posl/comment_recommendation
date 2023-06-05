def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    # dp[i][0] 表示第i个元素被替换的情况下的最小值
    # dp[i][1] 表示第i个元素不被替换的情况下的最小值
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    dp[1][0] = L
    dp[1][1] = 0
    for i in range(2, N+1):
        dp[i][0] = min(dp[i-1][0] + L, dp[i-1][1] + L)
        dp[i][1] = min(dp[i-1][0] + R, dp[i-1][1] + R)
    ans = float('inf')
    for i in range(1, N+1):
        ans = min(ans, dp[i][0]+(N-i)*R+A[i-1], dp[i][1]+(N-i)*R+A[i-1])
    print(ans)

if __name__ == '__main__':
    solve()