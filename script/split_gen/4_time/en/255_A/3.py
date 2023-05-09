def main():
    r, c = map(int, input().split())
    matrix = []
    for i in range(2):
        matrix.append(list(map(int, input().split())))
    print(matrix[r-1][c-1])
