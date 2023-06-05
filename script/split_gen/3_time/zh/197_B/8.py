def get_visible_count(grid, x, y):
    count = 0
    for i in range(x-1, -1, -1):
        if grid[i][y-1] == '#':
            break
        else:
            count += 1
    for i in range(x, len(grid)):
        if grid[i][y-1] == '#':
            break
        else:
            count += 1
    for i in range(y-1, -1, -1):
        if grid[x-1][i] == '#':
            break
        else:
            count += 1
    for i in range(y, len(grid[0])):
        if grid[x-1][i] == '#':
            break
        else:
            count += 1
    return count
