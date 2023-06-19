def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    MOD = 998244353
    DP = [[0] * 10 for _ in range(N)]
    DP[0][A[0]] = 1
    for i in range(1, N):
        for j in range(10):
            DP[i][j] = (DP[i][j] + DP[i-1][j] * 2) % MOD
            DP[i][(j + A[i]) % 10] = (DP[i][(j + A[i]) % 10] + DP[i-1][j]) % MOD
            DP[i][(j * A[i]) % 10] = (DP[i][(j * A[i]) % 10] + DP[i-1][j]) % MOD
    for i in range(10):
        print(DP[N-1][i])
solve()
