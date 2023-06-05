def print_matrix_element():
    r, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(2)]
    print(matrix[r-1][c-1])

if __name__ == '__main__':
    print_matrix_element()