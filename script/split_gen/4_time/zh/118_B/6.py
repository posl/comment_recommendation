def get_input():
    N, M = input().split()
    N, M = int(N), int(M)
    K = []
    A = []
    for i in range(N):
        k, a = input().split()
        k = int(k)
        a = [int(i) for i in a]
        K.append(k)
        A.append(a)
    return N, M, K, A
