def solve():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(input())
    for i in range(n-5):
        for j in range(n):
            if grid[i][j] == '#' and grid[i+1][j] == '#' and grid[i+2][j] == '#' and grid[i+3][j] == '#' and grid[i+4][j] == '#' and grid[i+5][j] == '#':
                print('Yes')
                return
    for i in range(n):
        for j in range(n-5):
            if grid[i][j] == '#' and grid[i][j+1] == '#' and grid[i][j+2] == '#' and grid[i][j+3] == '#' and grid[i][j+4] == '#' and grid[i][j+5] == '#':
                print('Yes')
                return
    for i in range(n-5):
        for j in range(n-5):
            if grid[i][j] == '#' and grid[i+1][j+1] == '#' and grid[i+2][j+2] == '#' and grid[i+3][j+3] == '#' and grid[i+4][j+4] == '#' and grid[i+5][j+5] == '#':
                print('Yes')
                return
    for i in range(5, n):
        for j in range(n-5):
            if grid[i][j] == '#' and grid[i-1][j+1] == '#' and grid[i-2][j+2] == '#' and grid[i-3][j+3] == '#' and grid[i-4][j+4] == '#' and grid[i-5][j+5] == '#':
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    solve()