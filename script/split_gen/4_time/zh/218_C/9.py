def read_input():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        T.append(input())
    return N, S, T
