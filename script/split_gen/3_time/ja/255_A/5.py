def main():
    R, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(2)]
    print(matrix[R-1][C-1])
