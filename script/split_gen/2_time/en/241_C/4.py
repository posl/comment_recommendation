def main():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(input())
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#':
                continue
            grid[i] = grid[i][:j] + '#' + grid[i][j+1:]
            for k in range(n):
                if grid[k][j] == '#':
                    continue
                grid[k] = grid[k][:j] + '#' + grid[k][j+1:]
                if check(grid):
                    print('Yes')
                    return
                grid[k] = grid[k][:j] + '.' + grid[k][j+1:]
            grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
    print('No')
