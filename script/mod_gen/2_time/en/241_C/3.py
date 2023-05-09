def main():
    N = int(input())
    grid = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                grid[i] = grid[i][:j] + '#' + grid[i][j+1:]
                if check(grid):
                    print('Yes')
                    return
                for k in range(N):
                    for l in range(N):
                        if grid[k][l] == '.':
                            grid[k] = grid[k][:l] + '#' + grid[k][l+1:]
                            if check(grid):
                                print('Yes')
                                return
                            grid[k] = grid[k][:l] + '.' + grid[k][l+1:]
                grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
    print('No')

if __name__ == '__main__':
    main()