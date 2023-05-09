def find_squares(grid):
    squares = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == '#':
                squares.append((i, j))
    return squares

if __name__ == '__main__':
    find_squares()