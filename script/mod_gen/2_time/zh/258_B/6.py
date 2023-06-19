def get_max_num(grid):
    max_num = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_num = max(max_num, int(grid[i][j]))
    return max_num

if __name__ == '__main__':
    get_max_num()