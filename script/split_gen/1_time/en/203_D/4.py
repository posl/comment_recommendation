def main():
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    def check(x):
        B = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(N):
                B[i + 1][j + 1] = B[i][j + 1] + B[i + 1][j] - B[i][j] + (A[i][j] < x)
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                if B[i + K][j + K] - B[i + K][j] - B[i][j + K] + B[i][j] < K * K // 2 + 1:
                    return True
        return False
    ok, ng = 0, 10 ** 9 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
