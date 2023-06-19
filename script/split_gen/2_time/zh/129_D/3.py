def getLightNum(h,w,grid):
    #上下左右
    up = [0 for i in range(w)]
    down = [0 for i in range(w)]
    left = [0 for i in range(h)]
    right = [0 for i in range(h)]
    #上
    for i in range(w):
        if grid[0][i] == "#":
            up[i] = 0
        else:
            up[i] = 1
    #下
    for i in range(w):
        if grid[h-1][i] == "#":
            down[i] = 0
        else:
            down[i] = 1
    #左
    for i in range(h):
        if grid[i][0] == "#":
            left[i] = 0
        else:
            left[i] = 1
    #右
    for i in range(h):
        if grid[i][w-1] == "#":
            right[i] = 0
        else:
            right[i] = 1
    #print(up,down,left,right)
    #上
    for i in range(w):
        if up[i] == 1:
            for j in range(1,h):
                if grid[j][i] == "#":
                    break
                else:
                    up[i] += 1
    #下
    for i in range(w):
        if down[i] == 1:
            for j in range(h-2,-1,-1):
                if grid[j][i] == "#":
                    break
                else:
                    down[i] += 1
    #左
    for i in range(h):
        if left[i] == 1:
            for j in range(1,w):
                if grid[i][j] == "#":
                    break
                else:
                    left[i] += 1
    #右
    for i in range(h):
        if right[i] == 1:
            for j in range(w-2,-1,-1):
                if grid[i][j] == "#":
                    break
                else:
                    right[i] += 1
    #print(up,down,left,right)
    #求最大值
    max = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#":
