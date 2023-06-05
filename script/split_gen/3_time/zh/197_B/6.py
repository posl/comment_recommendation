def check(x, y):
    if x < 0 or x >= H or y < 0 or y >= W:
        return False
    if grid[x][y] == '#':
        return False
    return True
