def clock(a,b,h,m):
    import math
    # 分针的角速度
    v_m = 360/60
    # 时针的角速度
    v_h = 360/12
    # 分针的角度
    angle_m = v_m*m
    # 时针的角度
    angle_h = v_h*h + v_h*m/60
    # 分针的坐标
    x_m = a*math.cos(math.radians(angle_m))
    y_m = a*math.sin(math.radians(angle_m))
    # 时针的坐标
    x_h = b*math.cos(math.radians(angle_h))
    y_h = b*math.sin(math.radians(angle_h))
    # 两个坐标之间的距离
    distance = math.sqrt((x_m-x_h)**2+(y_m-y_h)**2)
    return distance

if __name__ == '__main__':
    clock()