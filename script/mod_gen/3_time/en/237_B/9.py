def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    print_matrix()