def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N)]
    for i in range(N):
        dp[i][1 << i] = A[i][i]
    for i in range(1 << N):
        for j in range(N):
            if i & (1 << j):
                for k in range(N):
                    if i & (1 << k):
                        dp[j][i] = max(dp[j][i], dp[k][i ^ (1 << j)] ^ A[k][j])
    print(dp[0][(1 << N) - 1])
