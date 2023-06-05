def get_min_step(r, x, y):
    #步数
    step = 0
    #当前位置
    cur_x, cur_y = 0, 0
    while True:
        #到达终点
        if cur_x == x and cur_y == y:
            break
        #到达终点
        if cur_x == x and cur_y == -y:
            break
        #到达终点
        if cur_x == -x and cur_y == y:
            break
        #到达终点
        if cur_x == -x and cur_y == -y:
            break
        #到达终点
        if cur_x == y and cur_y == x:
            break
        #到达终点
        if cur_x == y and cur_y == -x:
            break
        #到达终点
        if cur_x == -y and cur_y == x:
            break
        #到达终点
        if cur_x == -y and cur_y == -x:
            break
        #到达终点
        if cur_x == x and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == y:
            break
        #到达终点
        if cur_x == -x and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == -y:
            break
        #到达终点
        if cur_x == y and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == -y:
            break
        #到达终点
        if cur_x == -y and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == -y:
            break
        #到达终点
        if cur_x == y and cur_y == 0:
            break
        #到达终点
        if cur_x == 0 and cur_y == y:
            break
        #到达终点
        if cur_x == -x and cur_y == 0

if __name__ == '__main__':
    get_min_step()