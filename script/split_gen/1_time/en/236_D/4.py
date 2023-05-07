def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[-1] * (1 << N) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(1 << N):
            if dp[i][j] == -1:
                continue
            for k in range(N):
                if (j >> k) & 1:
                    continue
                dp[i + 1][j | (1 << k)] = max(dp[i + 1][j | (1 << k)], dp[i][j] ^ A[i][k])
    print(dp[N][(1 << N) - 1])
