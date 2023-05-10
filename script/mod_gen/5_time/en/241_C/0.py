def main():
    n = int(input())
    grid = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                grid[i] = grid[i][:j] + '#' + grid[i][j+1:]
                if check(grid):
                    print('Yes')
                    return
                grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
    print('No')

if __name__ == '__main__':
    main()