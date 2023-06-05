def find_path(grid, x, y):
    #print(grid)
    #print(x, y)
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return -1
    if grid[x][y] == 'U':
        return find_path(grid, x-1, y)
    elif grid[x][y] == 'D':
        return find_path(grid, x+1, y)
    elif grid[x][y] == 'L':
        return find_path(grid, x, y-1)
    elif grid[x][y] == 'R':
        return find_path(grid, x, y+1)
    else:
        return [x+1, y+1]

if __name__ == '__main__':
    find_path()