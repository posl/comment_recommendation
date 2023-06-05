def main():
    N, M = map(int, input().split())
    M = M**0.5
    M = int(M)
    # print(M)
    grid = [[0]*N for i in range(N)]
    # print(grid)
    for i in range(N):
        for j in range(N):
            if (i==0 and j==0):
                grid[i][j] = 0
            elif (i==0):
                grid[i][j] = grid[i][j-1] + 1
            elif (j==0):
                grid[i][j] = grid[i-1][j] + 1
            else:
                grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + 1
    # print(grid)
    if (M==0):
        for i in range(N):
            for j in range(N):
                grid[i][j] = -1
    elif (M==1):
        for i in range(N):
            for j in range(N):
                if (i==0 and j==0):
                    grid[i][j] = 0
                elif (i==0):
                    grid[i][j] = grid[i][j-1] + 1
                elif (j==0):
                    grid[i][j] = grid[i-1][j] + 1
                else:
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + 1
    else:
        for i in range(N):
            for j in range(N):
                if (i==0 and j==0):
                    grid[i][j] = 0
                elif (i==0):
                    grid[i][j] = grid[i][j-1] + 1
                elif (j==0):
                    grid[i][j] = grid[i-1][j] + 1
                else:
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + 1
        for i in range(N):
            for j in range(N):
                if (grid[i][j] > M):
                    grid[i][j] = -1
    for i in range(N):
        for j in range(N):
            if (j == N-1):
                print
