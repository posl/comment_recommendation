def rotate_point(x, y, d):
    # x, y 是点的坐标
    # d 是旋转角度
    import math
    rad = math.radians(d)
    x1 = x * math.cos(rad) - y * math.sin(rad)
    y1 = x * math.sin(rad) + y * math.cos(rad)
    return x1, y1

if __name__ == '__main__':
    rotate_point()