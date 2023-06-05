def calc_angle(x1, y1, x2, y2, x3, y3):
    v1x = x2 - x1
    v1y = y2 - y1
    v2x = x3 - x2
    v2y = y3 - y2
    dot = v1x * v2x + v1y * v2y
    det = v1x * v2y - v1y * v2x
    angle = math.atan2(det, dot)
    return angle
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
angle1 = calc_angle(x1, y1, x2, y2, x3, y3)
angle2 = calc_angle(x2, y2, x3, y3, x4, y4)
angle3 = calc_angle(x3, y3, x4, y4, x1, y1)
angle4 = calc_angle(x4, y4, x1, y1, x2, y2)
