def solve(N, A, B):
    MOD = 998244353
    dp = [[0]*(3001) for _ in range(3001)]
    for i in range(A[0], B[0]+1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(3001):
            dp[i][j] = dp[i-1][j]
            if j >= A[i]:
                dp[i][j] += dp[i][j-1]
            if j > B[i]:
                dp[i][j] -= dp[i-1][j-1]
            dp[i][j] %= MOD
    return dp[N-1][3000]
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, A, B))

if __name__ == '__main__':
    solve()