def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (2**N) for _ in range(N + 1)]
    for i in range(N):
        for j in range(2**N):
            for k in range(i + 1, N):
                if j & (1 << k):
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j ^ (1 << k)] + A[i][k])
    print(dp[N][2**N - 1])
solve()

if __name__ == '__main__':
    solve()