def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    cumsum = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            cumsum[i + 1][j + 1] = cumsum[i + 1][j] + cumsum[i][j + 1] - cumsum[i][j] + A[i][j]
    def get_area(i, j):
        return cumsum[i + K][j + K] - cumsum[i + K][j] - cumsum[i][j + K] + cumsum[i][j]
    def get_median(i, j):
        arr = []
        for x in range(i, i + K):
            for y in range(j, j + K):
                arr.append(A[x][y])
        arr.sort()
        return arr[(K * K) // 2]
    ans = 10 ** 18
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            ans = min(ans, get_median(i, j))
    print(ans)

if __name__ == '__main__':
    main()