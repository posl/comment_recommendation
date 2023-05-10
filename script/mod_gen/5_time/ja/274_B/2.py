def count_boxs(grid, W):
    count = 0
    for i in range(W):
        if grid[i] == '#':
            count += 1
    return count

if __name__ == '__main__':
    count_boxs()