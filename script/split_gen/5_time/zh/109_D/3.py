def check_even(matrix, h, w):
    count = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] % 2 == 0:
                count += 1
    return count
