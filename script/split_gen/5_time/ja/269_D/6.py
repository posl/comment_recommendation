def solve():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    x.sort()
    y.sort()
    x_min = x[0]
    x_max = x[n-1]
    y_min = y[0]
    y_max = y[n-1]
    x_min -= 1
    x_max += 1
    y_min -= 1
    y_max += 1
    x.append(x_min)
    x.append(x_max)
    y.append(y_min)
    y.append(y_max)
    x.sort()
    y.sort()
    n += 2
    x_min_idx = x.index(x_min)
    x_max_idx = x.index(x_max)
    y_min_idx = y.index(y_min)
    y_max_idx = y.index(y_max)
    #print(x)
    #print(y)
    #print(x_min_idx)
    #print(x_max_idx)
    #print(y_min_idx)
    #print(y_max_idx)
    #print(n)
    grid = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        grid[i][i] = 1
    for i in range(n-1):
        grid[i][i+1] = 1
        grid[i+1][i] = 1
    for i in range(n-2):
        grid[i][i+2] = 1
        grid[i+2][i] = 1
    for i in range(n-3):
        grid[i][i+3] = 1
        grid[i+3][i] = 1
    for i in range(n-4):
        grid[i][i+4] = 1
        grid[i+4][i] = 1
    for i in range(n-5):
        grid[i][i+5] = 1
        grid[i+5][i] = 1
    #print(grid)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if (x_min_idx <= i and i <= x_max_idx) and (y_min_idx <= j and j <= y_max_idx
