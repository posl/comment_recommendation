Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    a,b,h,m = map(int,input().split())
    if h == 12:
        h = 0
    if m == 60:
        m = 0
    h_angle = 0.5 * (h*60 + m)
    m_angle = 6 * m
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    angle = math.radians(angle)
    print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle)))

=======
Suggestion 2

def main():
    a, b, h, m = map(int, input().split())
    # 時針と分針の角度
    h_angle = 30 * h + 0.5 * m
    m_angle = 6 * m
    # 時針と分針の角度差
    angle = abs(h_angle - m_angle)
    # 角度差をラジアンに変換
    rad = angle * math.pi / 180
    # 三平方の定理
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(rad))
    print(c)

=======
Suggestion 3

def main():
    a, b, h, m = map(int, input().split())
    print(a, b, h, m)

=======
Suggestion 4

def main():
  a, b, h, m = map(int, input().split())
  h_angle = (h * 60 + m) / 2
  m_angle = m * 6
  angle = min(abs(h_angle - m_angle), 360 - abs(h_angle - m_angle))
  print((a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle))) ** 0.5)

=======
Suggestion 5

def main():
    A, B, H, M = map(int, input().split())
    #時針と分針の角度を求める
    angle_hour = 30 * H + 0.5 * M
    angle_minute = 6 * M
    #時針と分針の角度の差を求める
    angle_diff = abs(angle_hour - angle_minute)
    #時針と分針の角度の差のラジアンを求める
    radian = math.radians(angle_diff)
    #時針と分針の角度の差のラジアンを用いて、時針と分針の端点の距離を求める
    distance = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(radian))
    print(distance)

=======
Suggestion 6

def main():
    A, B, H, M = map(int, input().split())
    #時針の角度
    theta = (H * 60 + M) * 360 / (12 * 60)
    #分針の角度
    phi = M * 360 / 60
    #時針と分針の角度差
    theta = abs(theta - phi)
    #時針と分針の角度差が180度以上なら、180度を引く
    if theta > 180:
        theta = 360 - theta
    #角度差をラジアンに変換
    theta = math.radians(theta)
    #cosθ = (A^2 + B^2 - C^2) / 2AB
    C = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta))
    print(C)

=======
Suggestion 7

def solve():
    A,B,H,M=map(int,input().split())
    H_angle=30*H+M/2
    M_angle=6*M
    angle=abs(H_angle-M_angle)
    if angle > 180:
        angle=360-angle
    angle=angle/180*math.pi
    print(math.sqrt(A**2+B**2-2*A*B*math.cos(angle)))

=======
Suggestion 8

def main():
    a,b,h,m = map(int,input().split())
    theta = (h*60+m)/720 * 2 * math.pi
    phi = m/60 * 2 * math.pi
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(theta-phi)))

=======
Suggestion 9

def main():
    A, B, H, M = map(int, input().split())
    # 時針の角度、分針の角度
    theta_h = (H * 60 + M) * 360 / (12 * 60)
    theta_m = M * 360 / 60
    # 2 本の針の角度差
    theta = abs(theta_h - theta_m)
    # 三角関数を使って、2 本の針の端点の距離を求める
    import math
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(theta))))
