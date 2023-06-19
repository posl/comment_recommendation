def get_min_error(grid, color, N, C):
    min_error = 0
    for i in range(N):
        for j in range(N):
            if (i+j)%3 == 0:
                min_error += grid[i][j] * color[0]
            elif (i+j)%3 == 1:
                min_error += grid[i][j] * color[1]
            elif (i+j)%3 == 2:
                min_error += grid[i][j] * color[2]
    return min_error

if __name__ == '__main__':
    get_min_error()