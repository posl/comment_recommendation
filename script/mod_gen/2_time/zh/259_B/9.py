def rotate(a,b,d):
    import math
    # 将角度转换为弧度
    d = math.radians(d)
    # 计算新的x坐标
    x = a * math.cos(d) - b * math.sin(d)
    # 计算新的y坐标
    y = a * math.sin(d) + b * math.cos(d)
    return x,y

if __name__ == '__main__':
    rotate()