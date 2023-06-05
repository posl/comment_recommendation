def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if i < j:
                for k in range(1 << (N - 1)):
                    if (k & (1 << (i - 1))) == 0 and (k & (1 << (j - 1))) == 0:
                        dp[i][k | (1 << (i - 1)) | (1 << (j - 1))] = max(dp[i][k | (1 << (i - 1)) | (1 << (j - 1))], dp[i + 1][k] + A[i][j])
    print(dp[0][(1 << N) - 1])

if __name__ == '__main__':
    main()