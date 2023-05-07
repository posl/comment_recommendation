def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    import itertools
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import shortest_path
    from scipy.sparse.csgraph import minimum_spanning_tree
    from scipy.sparse.csgraph import connected_components
    from scipy.sparse.csgraph import connected_co

if __name__ == '__main__':
    main()