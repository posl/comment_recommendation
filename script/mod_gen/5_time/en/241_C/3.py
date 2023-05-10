def check_for_consecutive_black_squares(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.':
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i + 5 < len(grid) and j + 5 < len(grid):
                if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3] + grid[i + 4][j + 4] + grid[i + 5][j + 5] == 6:
                    return True
            if i + 5 < len(grid):
                if grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j] + grid[i + 4][j] + grid[i + 5][j] == 6:
                    return True
            if j + 5 < len(grid):
                if grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i][j + 3] + grid[i][j + 4] + grid[i][j + 5] == 6:
                    return True
    return False

if __name__ == '__main__':
    check_for_consecutive_black_squares()