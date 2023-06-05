def solve():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0] * Q
    q = [0] * Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    # 为了方便起见，我们将L和R的元素都减1。
    for i in range(M):
        L[i] -= 1
        R[i] -= 1
    # 用二维数组C来记录答案。
    C = [[0] * N for i in range(N)]
    for i in range(M):
        for j in range(L[i], R[i] + 1):
            C[j][R[i]] += 1
    for i in range(N):
        for j in range(N - 1):
            C[i][j + 1] += C[i][j]
    for i in range(Q):
        print(C[p[i] - 1][q[i] - 1])
solve()
