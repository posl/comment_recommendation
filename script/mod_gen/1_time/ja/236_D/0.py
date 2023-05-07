def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for S in range(1 << N):
            for j in range(N):
                if (S >> j) & 1:
                    dp[i][S] = max(dp[i][S], dp[i - 1][S ^ (1 << j)] + A[i - 1][j])
    print(dp[N][(1 << N) - 1])

if __name__ == '__main__':
    main()