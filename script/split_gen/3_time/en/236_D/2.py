def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (2 ** N) for _ in range(N + 1)]
    for i in range(N):
        for j in range(2 ** N):
            for k in range(N):
                if (j >> k) & 1 == 0:
                    dp[i + 1][j | (1 << k)] = max(dp[i + 1][j | (1 << k)], dp[i][j] ^ A[i][k])
    print(dp[N][(2 ** N) - 1])
