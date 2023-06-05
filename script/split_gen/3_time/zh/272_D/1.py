def main():
    n,m = map(int,input().split())
    grid = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                grid[i][j] = 0
            elif i == 0:
                grid[i][j] = grid[i][j-1]+1
            elif j == 0:
                grid[i][j] = grid[i-1][j]+1
            else:
                grid[i][j] = min(grid[i][j-1],grid[i-1][j])+1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                grid[i][j] = 0
            else:
                grid[i][j] = grid[i][j]**2
                if grid[i][j] > m:
                    grid[i][j] = -1
    for i in range(n):
        print(' '.join(map(str,grid[i])))
