def check_black(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                return False
    return True

if __name__ == '__main__':
    check_black()