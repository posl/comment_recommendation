def main():
    # 读入数据
    a, b, h, m = map(int, input().split())
    # 计算时针和分针的角度
    angle_h = 30 * h + 0.5 * m
    angle_m = 6 * m
    # 计算时针和分针的坐标
    x_h = a * math.cos(math.radians(angle_h))
    y_h = a * math.sin(math.radians(angle_h))
    x_m = b * math.cos(math.radians(angle_m))
    y_m = b * math.sin(math.radians(angle_m))
    # 计算两个坐标之间的距离
    print(math.sqrt((x_h - x_m) ** 2 + (y_h - y_m) ** 2))
