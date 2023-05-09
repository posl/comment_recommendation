def main():
    h, w = map(int, input().split())
    matrix = []
    for i in range(h):
        matrix.append(list(input()))
    matrix = list(zip(*matrix))
    for i in range(w):
        matrix[i] = list(matrix[i])
    for i in range(w):
        matrix[i] = matrix[i].count('#')
    print(*matrix)

if __name__ == '__main__':
    main()