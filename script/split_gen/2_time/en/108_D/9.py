def generate_graph(L):
    N = 20
    M = 60
    edges = []
    for i in range(1, N):
        edges.append((i, i + 1, 0))
        for j in range(1, i):
            edges.append((j, i + 1, 1))
    for i in range(1, N):
        edges.append((i, i + 1, 2))
    for i in range(1, L):
        edges.append((i, i + 1, 3))
    return N, M, edges
