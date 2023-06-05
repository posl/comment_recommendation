Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,h,m = map(int,input().split())
    h_angle = (h+m/60)/12*360
    m_angle = m/60*360
    angle = abs(h_angle-m_angle)
    angle = angle if angle<180 else 360-angle
    import math
    angle = angle*math.pi/180
    import decimal
    decimal.getcontext().prec = 100
    print(decimal.Decimal(a**2+b**2-2*a*b*math.cos(angle)).sqrt())

=======
Suggestion 2

def main():
    a,b,h,m=map(int,input().split())
    import math
    h=h+m/60
    h=h/12
    m=m/60
    m=math.fabs(h-m)
    m=m*2*math.pi
    m=math.cos(m)
    m=math.pow(a,2)+math.pow(b,2)-2*a*b*m
    m=math.sqrt(m)
    print(m)

=======
Suggestion 3

def main():
    a,b,h,m = map(int,input().split())
    import math
    ans = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(abs(30*h - 5.5*m))))
    print(ans)

=======
Suggestion 4

def clock():
    a,b,h,m = map(int, input().split())
    hour = h + m/60
    hour_angle = hour * 30
    minute_angle = m * 6
    angle = abs(hour_angle - minute_angle)
    if angle > 180:
        angle = 360 - angle
    import math
    angle = math.radians(angle)
    c = (a**2 + b**2 - 2*a*b*math.cos(angle))**0.5
    print(c)

clock()

=======
Suggestion 5

def clock(a,b,h,m):
    import math
    angle = math.pi/6*h-m*math.pi/30
    return math.sqrt(a**2+b**2-2*a*b*math.cos(angle))

print(clock(3,4,9,0))
print(clock(3,4,10,40))

=======
Suggestion 6

def main():
    a,b,h,m = map(int,input().split())
    import math
    h_a = 30*h + m/2
    b_a = 6*m
    #print(h_a,b_a)
    #print(math.cos(math.radians(h_a)))
    #print(math.cos(math.radians(b_a)))
    print(math.sqrt(a**2+b**2-2*a*b*(math.cos(math.radians(h_a-b_a)))))

=======
Suggestion 7

def main():
    a, b, h, m = map(int, input().split())
    print(a**2 + b**2 - 2*a*b*(math.cos(math.pi*(h/6 - m/30))))

=======
Suggestion 8

def input():
    a, b, h, m = map(int, raw_input().split())
    return a, b, h, m

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    import math
    a,b,h,m = map(int, input().split())
    h_theta = 30*h + 0.5*m
    m_theta = 6*m
    theta = abs(h_theta - m_theta)
    if theta > 180:
        theta = 360 - theta
    theta = theta * math.pi / 180
    print((a**2 + b**2 - 2*a*b*math.cos(theta))**0.5)
