def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    A = [[0] * (N + 1)] + [[0] + a for a in A]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            A[i][j] += A[i - 1][j] + A[i][j - 1] - A[i - 1][j - 1]
    ok, ng = 0, 10 ** 9 + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        ok_flag = False
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                if A[i + K][j + K] - A[i + K][j] - A[i][j + K] + A[i][j] <= mid * K ** 2:
                    ok_flag = True
        if ok_flag:
            ng = mid
        else:
            ok = mid
    print(ng)
