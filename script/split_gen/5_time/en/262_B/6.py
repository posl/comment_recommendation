def get_input():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        U, V = map(int, input().split())
        edges.append((U, V))
    return N, M, edges
