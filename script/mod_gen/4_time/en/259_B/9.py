def rotate(a, b, d):
    # 2d matrix
    matrix = [[0 for i in range(2)] for j in range(2)]
    matrix[0][0] = math.cos(math.radians(d))
    matrix[0][1] = -1 * math.sin(math.radians(d))
    matrix[1][0] = math.sin(math.radians(d))
    matrix[1][1] = math.cos(math.radians(d))
    # 2d vector
    vector = [[0 for i in range(1)] for j in range(2)]
    vector[0][0] = a
    vector[1][0] = b
    # multiply matrix and vector
    result = [[0 for i in range(1)] for j in range(2)]
    for i in range(len(matrix)):
        for j in range(len(vector[0])):
            for k in range(len(vector)):
                result[i][j] += matrix[i][k] * vector[k][j]
    return result[0][0], result[1][0]

if __name__ == '__main__':
    rotate()