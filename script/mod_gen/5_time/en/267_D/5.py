def solve(N, M, A):
    A.sort(reverse=True)
    dp = [[-float('inf') for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(M+1):
            if j > i+1:
                break
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + A[i] * j)
    return dp[N][M]
N, M = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, M, A))

if __name__ == '__main__':
    solve()