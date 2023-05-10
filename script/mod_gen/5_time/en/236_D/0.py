def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N):
        for j in range(i + 1, N):
            dp[j + 1][1 << i | 1 << j] = A[i][j]
    for i in range(1, N):
        for j in range(1 << N):
            if j >> i & 1:
                for k in range(1 << N):
                    if k >> i & 1:
                        dp[i + 1][j | k] = max(dp[i + 1][j | k], dp[i][k] + dp[i + 1][j])
    print(dp[N][(1 << N) - 1])

if __name__ == '__main__':
    main()