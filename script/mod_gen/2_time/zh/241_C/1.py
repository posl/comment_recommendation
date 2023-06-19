def check(grid, x, y):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return False
    if grid[x][y] == '#':
        return True
    return False

if __name__ == '__main__':
    check()