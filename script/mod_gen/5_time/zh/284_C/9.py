def set_adjacency_matrix(N, M, u, v):
    adjacency_matrix = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        adjacency_matrix[u[i]-1][v[i]-1] = 1
        adjacency_matrix[v[i]-1][u[i]-1] = 1
    return adjacency_matrix

if __name__ == '__main__':
    set_adjacency_matrix()