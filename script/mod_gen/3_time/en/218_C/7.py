def find_top_left(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                return (i, j)

if __name__ == '__main__':
    find_top_left()