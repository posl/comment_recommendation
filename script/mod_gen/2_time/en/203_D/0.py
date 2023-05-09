def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j] + A[i][j]
    ans = 10 ** 18
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            x = B[i + K][j + K] - B[i + K][j] - B[i][j + K] + B[i][j]
            ans = min(ans, x)
    print(ans)

if __name__ == '__main__':
    main()