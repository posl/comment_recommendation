def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

if __name__ == '__main__':
    transpose_matrix()