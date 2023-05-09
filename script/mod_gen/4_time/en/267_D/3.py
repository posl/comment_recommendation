def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    dp = [[-1]*(N+1) for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(1,M+1):
        for j in range(i,N+1):
            dp[i][j] = max(dp[i-1][j-1]+A[j-1], dp[i][j-1])
    ans = 0
    for i in range(1,M+1):
        ans = max(ans, dp[i][N] + i * S[N-i])
    print(ans)
    return 0

if __name__ == '__main__':
    solve()