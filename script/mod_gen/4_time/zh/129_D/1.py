def get_max_light_num(h,w,grid):
    light_num = 0
    for i in range(1,h+1):
        for j in range(1,w+1):
            if grid[i][j] == '#':
                continue
            else:
                light_num = max(light_num, get_light_num(i,j,h,w,grid))
    return light_num

if __name__ == '__main__':
    get_max_light_num()