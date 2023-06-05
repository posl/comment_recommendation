def get_max_num(matrix):
    max_num = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            max_num = max(max_num, matrix[i][j])
    return max_num
