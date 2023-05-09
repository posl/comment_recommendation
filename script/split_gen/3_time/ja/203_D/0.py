def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j] + A[i][j]
    ans = 10 ** 10
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            k = K ** 2 // 2 + 1
            l = -1
            r = 10 ** 9 + 1
            while r - l > 1:
                m = (l + r) // 2
                s = B[i + K][j + K] - B[i + K][j] - B[i][j + K] + B[i][j]
                if s >= m * k:
                    r = m
                else:
                    l = m
            ans = min(ans, r)
    print(ans)
