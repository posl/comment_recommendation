def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    def check(x):
        B = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                B[i + 1][j + 1] = B[i + 1][j] + B[i][j + 1] - B[i][j] + (1 if A[i][j] >= x else 0)
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                if B[i + K][j + K] - B[i + K][j] - B[i][j + K] + B[i][j] >= (K * K + 1) // 2:
                    return True
        return False
    l, r = -1, 10 ** 9 + 1
    while r - l > 1:
        c = (l + r) // 2
        if check(c):
            l = c
        else:
            r = c
    print(l)
