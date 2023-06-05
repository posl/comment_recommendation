def rotate_90_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    res = [[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][n-1-i] = matrix[i][j]
    return res

if __name__ == '__main__':
    rotate_90_clockwise()