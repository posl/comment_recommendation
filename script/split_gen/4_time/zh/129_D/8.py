def get_max_lighted_square_area(grid):
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                continue
            area = 1
            for k in range(i-1, -1, -1):
                if grid[k][j] == '#':
                    break
                area += 1
            for k in range(i+1, len(grid)):
                if grid[k][j] == '#':
                    break
                area += 1
            for k in range(j-1, -1, -1):
                if grid[i][k] == '#':
                    break
                area += 1
            for k in range(j+1, len(grid[0])):
                if grid[i][k] == '#':
                    break
                area += 1
            if area > max_area:
                max_area = area
    return max_area
