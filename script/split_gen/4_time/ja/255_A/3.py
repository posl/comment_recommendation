def main():
    r, c = map(int, input().split())
    matrix = []
    for i in range(r):
        matrix.append(list(map(int, input().split())))
    print(matrix[r-1][c-1])
