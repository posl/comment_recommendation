def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(2*N-1)]
    dp = [[0]*(2**N) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(2**i):
            for k in range(2*N-2*i):
                dp[i+1][j|(1<<k)] = max(dp[i+1][j|(1<<k)], dp[i][j] ^ A[i][k])
    print(dp[N][2**N-1])
solve()

if __name__ == '__main__':
    solve()