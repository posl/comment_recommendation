def isPassable(s_x, s_y, t_x, t_y, x, y, r):
    if s_x == t_x and s_y == t_y:
        return True
    # 两点连线方程
    a = s_y - t_y
    b = t_x - s_x
    c = s_x * t_y - t_x * s_y
    # 圆心到直线距离
    d = abs(a * x + b * y + c) / (a ** 2 + b ** 2) ** 0.5
    if d > r:
        return False
    # 两点距离
    dis = ((s_x - t_x) ** 2 + (s_y - t_y) ** 2) ** 0.5
    if dis <= r:
        return True
    return False
