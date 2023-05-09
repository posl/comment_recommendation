def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    dp = [[0] * (1 << N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i < j:
                dp[i][1 << i | 1 << j] = A[i][j]
    for i in range(1 << N):
        for j in range(N):
            if i & 1 << j:
                for k in range(N):
                    if i & 1 << k:
                        dp[k][i] = max(dp[k][i], dp[k][i ^ 1 << j] + A[k][j])
    print(dp[N - 1][(1 << N) - 1])
