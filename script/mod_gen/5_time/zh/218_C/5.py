def get_rotate_matrix(matrix):
    """
    顺时针旋转矩阵90度
    :param matrix: list[list[]]
    :return:
    """
    n = len(matrix)
    rotate_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            rotate_matrix[i][j] = matrix[n - 1 - j][i]
    return rotate_matrix

if __name__ == '__main__':
    get_rotate_matrix()