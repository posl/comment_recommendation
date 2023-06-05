Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b,h,m = map(int, input().split())
    import math
    x = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(abs(30*h-5.5*m))))
    print(x)

=======
Suggestion 2

def main():
    a, b, h, m = map(int, input().split())
    h_theta = (h + m / 60) * 30
    m_theta = m * 6
    from math import cos, pi
    print((a ** 2 + b ** 2 - 2 * a * b * cos((h_theta - m_theta) / 180 * pi)) ** 0.5)

=======
Suggestion 3

def main():
    a, b, h, m = map(int, input().split())
    h_angle = (h * 60 + m) / 720 * 360
    m_angle = m / 60 * 360
    angle = abs(h_angle - m_angle)
    import math
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle))))

=======
Suggestion 4

def main():
    a,b,h,m = map(int,input().split())
    import math
    x = math.radians(30*h+0.5*m)
    y = math.radians(6*m)
    import math
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(x-y)))

=======
Suggestion 5

def calc_distance(a, b, h, m):
    h_angle = 30 * h + 0.5 * m
    m_angle = 6 * m
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    return (a ** 2 + b ** 2 - 2 * a * b * cos(angle * pi / 180)) ** 0.5

=======
Suggestion 6

def cal_angle(hour,minute):
    return abs(30*hour-5.5*minute)

=======
Suggestion 7

def solve():
    import math
    a,b,h,m = map(int,input().split())
    h_angle = 2*math.pi*(h/12 + m/(12*60))
    m_angle = 2*math.pi*(m/60)
    x = a*math.cos(h_angle) - b*math.cos(m_angle)
    y = a*math.sin(h_angle) - b*math.sin(m_angle)
    print(math.sqrt(x*x + y*y))

=======
Suggestion 8

def getDistance(a, b, h, m):
    if h >= 12:
        h = h - 12
    h = h + m/60
    if h >= 12:
        h = h - 12
    h = h * 30
    m = m * 6
    angle = abs(h - m)
    if angle > 180:
        angle = 360 - angle
    angle = angle * 3.1415926535897932384626433832795 / 180
    return (a ** 2 + b ** 2 - 2 * a * b * cos(angle)) ** 0.5

=======
Suggestion 9

def problem168_c():
    pass

=======
Suggestion 10

def main():
    a, b, h, m = map(int, input().split())
    from math import cos, pi
    x = (h + m / 60) * pi / 6
    y = m * pi / 30
    from math import sqrt
    print(sqrt(a**2 + b**2 - 2 * a * b * cos(x - y)))
