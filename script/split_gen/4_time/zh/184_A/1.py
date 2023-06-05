def main():
    matrix = []
    for i in range(2):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(matrix)
    print(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
