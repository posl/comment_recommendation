def get_max_value(grid, N):
    max_value = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += max(grid[i][j-1], grid[i-1][j])
            if i+j == N-1 and max_value < grid[i][j]:
                max_value = grid[i][j]
    return max_value
