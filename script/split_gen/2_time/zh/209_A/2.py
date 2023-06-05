def main():
    N, M = map(int, input().split())
    A, B, C = [], [], []
    for i in range(M):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    # Floyd–Warshall algorithm
    # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    # https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
    # https://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/
    # https://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph/
    # https://www.geeksforgeeks.org/shortest-path-with-exactly-k-edges-in-a-directed-and-weighted-graph-set-2/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-2/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-3/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-4/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-5-dijkstra-clone/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-6-dag/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-7-dynamic-programming/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-8-dynamic-programming-2/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-9-oeksp-using-matrix-power/
    # https://www.geeksforgeeks.org/shortest-path-exactly-k-edges-directed-weighted-graph-set-10-dp-optimization/
    # https://www.geeksforgeeks.org/shortest-path-exactly
