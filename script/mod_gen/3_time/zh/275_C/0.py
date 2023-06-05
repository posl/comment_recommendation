def main():
    #input
    squares = []
    for i in range(9):
        squares.append(input())
    #solve
    count = 0
    for i in range(8):
        for j in range(8):
            if squares[i][j] == '#' and squares[i][j+1] == '#' and squares[i+1][j] == '#' and squares[i+1][j+1] == '#':
                count += 1
    #output
    print(count)

if __name__ == '__main__':
    main()