def find_min_dist(x,y,grid):
    if grid[x][y] != -1:
        return grid[x][y]
    else:
        min_dist = 1000000
        for i in range(N):
            for j in range(N):
                if grid[i][j] != -1:
                    dist = ((x-i)**2 + (y-j)**2)**0.5
                    if dist.is_integer():
                        min_dist = min(min_dist, grid[i][j] + dist)
        grid[x][y] = min_dist
        return min_dist
N,M = map(int, input().split())
grid = [[-1 for _ in range(N)] for _ in range(N)]
grid[0][0] = 0
for i in range(N):
    for j in range(N):
        find_min_dist(i,j,grid)
for row in grid:
    print(" ".join(map(str,row)))
