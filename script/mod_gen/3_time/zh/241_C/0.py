def isOK(matrix):
    for i in range(0, len(matrix)-5):
        for j in range(0, len(matrix)-5):
            if matrix[i][j] == '#' and matrix[i+1][j+1] == '#' and matrix[i+2][j+2] == '#' and matrix[i+3][j+3] == '#' and matrix[i+4][j+4] == '#' and matrix[i+5][j+5] == '#':
                return True
    return False
N = int(input())
matrix = []
for i in range(0, N):
    matrix.append(list(input()))

if __name__ == '__main__':
    isOK()