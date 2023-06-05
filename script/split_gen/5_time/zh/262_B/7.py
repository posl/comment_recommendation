def func(n, m, u, v):
    # 1. get the adjacent matrix
    adjacent_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        adjacent_matrix[u[i] - 1][v[i] - 1] = 1
        adjacent_matrix[v[i] - 1][u[i] - 1] = 1
    # 2. get the number of triangles
    num = 0
    for i in range(n):
        for j in range(i + 1, n):
            if adjacent_matrix[i][j] == 1:
                for k in range(j + 1, n):
                    if adjacent_matrix[i][k] == 1 and adjacent_matrix[j][k] == 1:
                        num += 1
    return num
