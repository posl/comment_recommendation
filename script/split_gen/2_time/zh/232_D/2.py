def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    for i in range(M):
        A[i] -= 1
        B[i] -= 1
        C[i] -= 1
        D[i] -= 1
    def calc(state):
        res = 0
        for i in range(M):
            if (state >> A[i]) & 1 and (state >> B[i]) & 1:
                res |= 1 << i
            if (state >> C[i]) & 1 and (state >> D[i]) & 1:
                res |= 1 << i
        return res
    ok = True
    for state in range(1 << N):
        if bin(state).count('1') != N // 2:
            continue
        if calc(state) == (1 << M) - 1:
            print('Yes')
            return
    print('No')
