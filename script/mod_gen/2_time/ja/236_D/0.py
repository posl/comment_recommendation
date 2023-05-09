def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            for k in range(1 << N):
                if k & (1 << j):
                    dp[i + 1][k] = max(dp[i + 1][k], dp[i][k ^ (1 << j)] + A[i][j])
    print(dp[N][-1])

if __name__ == '__main__':
    main()