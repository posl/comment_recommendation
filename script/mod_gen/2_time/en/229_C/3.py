def solve():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j >= B[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-B[i]] + A[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(dp[N][W])

if __name__ == '__main__':
    solve()