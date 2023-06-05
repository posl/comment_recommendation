def solve(N, A, B):
    MOD = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(A[i-1], B[i-1]+1):
            dp[i][j] = sum(dp[i-1][:j+1]) % MOD
    return sum(dp[N]) % MOD
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, A, B))
