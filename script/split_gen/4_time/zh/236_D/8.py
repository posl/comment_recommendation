def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][1 << j] = A[i][j]
    for i in range(N):
        for j in range(1 << N):
            if not dp[i + 1][j]: continue
            for k in range(N):
                if j >> k & 1: continue
                dp[i + 1][j | 1 << k] = max(dp[i + 1][j | 1 << k], dp[i + 1][j] + A[i][k])
    print(dp[N][(1 << N) - 1])
