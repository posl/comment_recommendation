def rotate90(n,matrix):
    new_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[j][n-i-1] = matrix[i][j]
    return new_matrix
