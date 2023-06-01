Synthesizing 10/10 solutions

=======
Suggestion 1

def problem168_c():
    # 读入数据
    a, b, h, m = map(int, input().split())

    # 时针和分针的角度
    theta_h = h * 30 + m / 2
    theta_m = m * 6

    # 时针和分针的坐标
    x_h = a * math.cos(math.radians(theta_h))
    y_h = a * math.sin(math.radians(theta_h))
    x_m = b * math.cos(math.radians(theta_m))
    y_m = b * math.sin(math.radians(theta_m))

    # 时针和分针的距离
    ans = math.sqrt((x_h - x_m) ** 2 + (y_h - y_m) ** 2)
    print(ans)

=======
Suggestion 2

def clock():
    import math
    import sys

    # 读取输入
    a, b, h, m = map(int, sys.stdin.readline().strip().split())

    # 计算角度
    angle = abs(30 * h + 0.5 * m - 6 * m)

    # 计算距离
    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))

    # 打印答案
    print(ans)

=======
Suggestion 3

def get_angle(H, M):
    return 30*H + 0.5*M

=======
Suggestion 4

def main():
    a, b, h, m = map(int, input().split())
    import math
    pi = math.pi
    h_angle = (h * 60 + m) / 720 * 2 * pi
    m_angle = m / 60 * 2 * pi
    h_x = a * math.cos(h_angle)
    h_y = a * math.sin(h_angle)
    m_x = b * math.cos(m_angle)
    m_y = b * math.sin(m_angle)
    print(math.sqrt((h_x - m_x) ** 2 + (h_y - m_y) ** 2))

=======
Suggestion 5

def get_distance(a, b, h, m):
    h_angle = (h + m / 60) * 30
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    return (a ** 2 + b ** 2 - 2 * a * b * cos(angle * pi / 180)) ** 0.5


a, b, h, m = map(int, input().split())
print(get_distance(a, b, h, m))

=======
Suggestion 6

def main():
    import math
    a, b, h, m = map(int, input().split())
    h_angle = 30 * h + 0.5 * m
    m_angle = 6 * m
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    angle = angle * math.pi / 180
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle)))

=======
Suggestion 7

def main():
    import math
    a,b,h,m = map(int, input().split())
    h_angle = (h*60 + m) * 0.5
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(angle)))
    print(c)

=======
Suggestion 8

def clock_angle(hour, minute):
    hour_angle = (hour % 12 + minute / 60.0) * 30.0
    minute_angle = minute * 6.0
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    return angle

=======
Suggestion 9

def main():
    a, b, h, m = map(int, input().split())
    import math
    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(abs(h * 30 + m * 0.5 - m * 6) * math.pi / 180))
    print(c)

=======
Suggestion 10

def main():
    a, b, h, m = map(int, input().split())
    import math
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(abs(30*h-5.5*m)))))
