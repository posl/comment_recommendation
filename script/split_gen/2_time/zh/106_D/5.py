def read_input():
    #input = sys.stdin.readline
    #N, M, Q = list(map(int, input().split()))
    #L = [0] * M
    #R = [0] * M
    #for i in range(M):
    #    L[i], R[i] = list(map(int, input().split()))
    #P = [0] * Q
    #Q = [0] * Q
    #for i in range(Q):
    #    P[i], Q[i] = list(map(int, input().split()))
    N, M, Q = 10, 10, 10
    L = [1, 2, 4, 4, 4, 5, 6, 6, 7, 10]
    R = [6, 9, 5, 7, 7, 8, 6, 7, 9, 10]
    P = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1]
    Q = [8, 9, 10, 8, 9, 10, 8, 9, 10, 10]
    return N, M, Q, L, R, P, Q
