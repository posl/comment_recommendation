def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for S in range(1 << N):
            if S >> i & 1 == 0:
                for j in range(i + 1, N):
                    if S >> j & 1 == 1:
                        dp[i][S] = max(dp[i][S], dp[j][S ^ (1 << i)] ^ A[i][j])
    print(dp[0][(1 << N) - 1])

if __name__ == '__main__':
    main()