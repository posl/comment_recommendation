def get_input():
    N, M = map(int, raw_input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, raw_input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, raw_input().split())
        C.append(c)
        D.append(d)
    return N, M, A, B, C, D
