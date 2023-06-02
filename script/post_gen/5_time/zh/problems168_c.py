Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, h, m = map(int, input().split())
    x = a * (h * 60 + m) / 720
    y = b * m / 60
    print((x ** 2 + y ** 2) ** 0.5)

=======
Suggestion 2

def clockHand(a, b, h, m):
    import math
    # 时针转动的角度
    h_angle = 30 * h + 0.5 * m
    # 分针转动的角度
    m_angle = 6 * m
    # 两个指针之间的角度
    angle = abs(h_angle - m_angle)
    # 余弦定理求出两个指针之间的距离
    c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(angle)))
    return c

=======
Suggestion 3

def main():
    a, b, h, m = map(int, input().split())
    import math
    x = (h + m / 60) * 30
    y = m * 6
    z = (x - y) % 360
    if z > 180:
        z = 360 - z
    z = math.radians(z)
    print((a ** 2 + b ** 2 - 2 * a * b * math.cos(z)) ** 0.5)

=======
Suggestion 4

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

=======
Suggestion 5

def main():
    # 读入输入
    a, b, h, m = map(int, input().split())
    # 计算角度
    a_rad = 2 * 3.14159265358979323846 * (h / 12 + m / 60 / 12)
    b_rad = 2 * 3.14159265358979323846 * (m / 60)
    # 计算距离
    import math
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(a_rad - b_rad)))

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    a, b, h, m = map(int, input().split())
    from math import cos, pi
    print((a**2+b**2-2*a*b*cos((h*60+m)*pi/360))**0.5)

=======
Suggestion 8

def clock_distance(a, b, h, m):
    h_angle = h * 30 + m * 0.5
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    angle = angle * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 / 180
    return (a ** 2 + b ** 2 - 2 * a * b * cos(angle)) ** 0.5

=======
Suggestion 9

def main():
    A, B, H, M = map(int, input().split())
    import math

    # 角度をラジアンに変換
    H_rad = (H * 60 + M) / 720 * math.pi * 2
    M_rad = M / 60 * math.pi * 2

    # 余弦定理
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(H_rad - M_rad)))

=======
Suggestion 10

def clock(a,b,h,m):
    if h > 12:
        h = h - 12
    h = h + m/60
    h = h * 30
    m = m * 6
    angle = abs(h - m)
    if angle > 180:
        angle = 360 - angle
    angle = angle * 3.1415926535897932384626433832795 / 180
    c = a**2 + b**2 - 2*a*b * math.cos(angle)
    c = math.sqrt(c)
    return c

import math
a,b,h,m = map(int,input().split())
print(clock(a,b,h,m))
