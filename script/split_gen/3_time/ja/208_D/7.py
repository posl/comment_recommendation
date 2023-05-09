def get_input():
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    C = [0]*M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    return N, M, A, B, C
