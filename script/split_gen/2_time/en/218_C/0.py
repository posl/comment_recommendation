def read_input():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        S.append(input())
    for _ in range(N):
        T.append(input())
    return N, S, T
