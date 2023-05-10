def main():
    N,M = map(int, input().rstrip().split())
    grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            grid[i][j] = (i-j)**2+(i+j)**2
    for i in range(N):
        for j in range(N):
            grid[i][j] = int(grid[i][j]**0.5)
    for i in range(N):
        for j in range(N):
            if grid[i][j]**2 == (i-j)**2+(i+j)**2:
                grid[i][j] = -1
    for i in range(N):
        print(' '.join(map(str, grid[i])))
