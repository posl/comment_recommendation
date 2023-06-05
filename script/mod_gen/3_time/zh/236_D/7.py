def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(1 << N)]
    for S in range(1 << N):
        for i in range(N):
            if (S >> i) & 1 == 0:
                continue
            for j in range(i + 1, N):
                if (S >> j) & 1 == 0:
                    continue
                dp[S][i] = max(dp[S][i], dp[S - (1 << i)][j] + A[j][i])
    print(max(dp[-1]))

if __name__ == '__main__':
    main()