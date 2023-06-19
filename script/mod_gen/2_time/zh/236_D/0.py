def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            dp[i + 1][1 << i | 1 << j] = A[i][j]
    for i in range(1, 1 << N):
        for j in range(N):
            if i >> j & 1:
                for k in range(N):
                    if i >> k & 1:
                        dp[k + 1][i] = max(dp[k + 1][i], dp[k + 1][i ^ 1 << j] + A[k][j])
    print(dp[N][(1 << N) - 1])

if __name__ == '__main__':
    main()