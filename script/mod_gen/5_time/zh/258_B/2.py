def get_max_num(N, grid):
    max_num = 0
    for i in range(N):
        for j in range(N):
            max_num = max(max_num, grid[i][j])
    return max_num

if __name__ == '__main__':
    get_max_num()