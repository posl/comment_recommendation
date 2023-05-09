def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N)]
    dp[0][0] = A[0][0]
    for i in range(1, N):
        for j in range(1 << i):
            for k in range(i):
                if (j >> k) & 1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - (1 << k)] + A[i][k])
            dp[i][j] += A[i][i]
    print(dp[N - 1][(1 << N) - 1])

if __name__ == '__main__':
    main()