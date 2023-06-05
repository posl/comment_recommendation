def get_input():
    N = int(input())
    T = []
    K = []
    A = []
    for i in range(N):
        t, k, *a = map(int, input().split())
        T.append(t)
        K.append(k)
        A.append(a)
    return N, T, K, A
