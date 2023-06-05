def get_graph(L):
    N = L + 1
    M = 2 * L - 1
    graph = []
    for i in range(1, L):
        graph.append((i, i + 1, 0))
    for i in range(1, L - 1):
        graph.append((i, i + 2, 2 * i - 1))
    for i in range(1, L - 2):
        graph.append((i, i + 3, 2 * i))
    for i in range(1, L - 3):
        graph.append((i, i + 4, 2 * i + 1))
    return N, M, graph

if __name__ == '__main__':
    get_graph()