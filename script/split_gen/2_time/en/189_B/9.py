def get_input():
    N, X = map(int, input().split())
    V = []
    P = []
    for _ in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    return N, X, V, P
