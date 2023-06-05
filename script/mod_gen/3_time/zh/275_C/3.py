def main():
    matrix = []
    for i in range(9):
        matrix.append(input())
    count = 0
    for i in range(1, 8):
        for j in range(1, 8):
            if matrix[i][j] == "#":
                if matrix[i-1][j-1] == "#" and matrix[i-1][j] == "#" and matrix[i][j-1] == "#":
                    count += 1
    print(count)

if __name__ == '__main__':
    main()