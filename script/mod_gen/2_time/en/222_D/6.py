def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0 for _ in range(3010)] for _ in range(3010)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j]
            dp[i+1][j] %= MOD
    print(dp[N][B[N-1]])
solve()

if __name__ == '__main__':
    solve()