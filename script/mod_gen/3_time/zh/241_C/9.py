def check_6x6(grid):
    for i in range(len(grid) - 5):
        for j in range(len(grid) - 5):
            if grid[i][j] == "#" and grid[i][j + 1] == "#" and grid[i][j + 2] == "#" and grid[i][j + 3] == "#" and \
                    grid[i][j + 4] == "#" and grid[i][j + 5] == "#" and grid[i + 1][j] == "#" and grid[i + 1][
                j + 1] == "#" and grid[i + 1][j + 2] == "#" and grid[i + 1][j + 3] == "#" and grid[i + 1][
                j + 4] == "#" and grid[i + 1][j + 5] == "#" and grid[i + 2][j] == "#" and grid[i + 2][
                j + 1] == "#" and grid[i + 2][j + 2] == "#" and grid[i + 2][j + 3] == "#" and grid[i + 2][
                j + 4] == "#" and grid[i + 2][j + 5] == "#" and grid[i + 3][j] == "#" and grid[i + 3][
                j + 1] == "#" and grid[i + 3][j + 2] == "#" and grid[i + 3][j + 3] == "#" and grid[i + 3][
                j + 4] == "#" and grid[i + 3][j + 5] == "#" and grid[i + 4][j] == "#" and grid[i + 4][
                j + 1] == "#" and grid[i + 4][j + 2] == "#" and grid[i + 4][j + 3] == "#" and grid[i + 4][
                j + 4] == "#" and grid[i + 4][j + 5] == "#" and grid[i + 5][j] == "#" and grid[i + 5][
                j + 1] == "#" and grid[i + 5][j + 2] == "#" and grid[i + 5][j + 3] == "#" and grid[i + 5][

if __name__ == '__main__':
    check_6x6()