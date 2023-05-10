def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(1 << N)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][1 << j] = max(dp[i + 1][1 << j], dp[i][0] ^ A[i][j])
        for j in range(1 << N):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i + 1][j & -j], dp[i][j])
            for k in range(N):
                dp[i + 1][j | (1 << k)] = max(dp[i + 1][j | (1 << k)], dp[i + 1][j] ^ A[i][k])
    print(dp[N][(1 << N) - 1])
