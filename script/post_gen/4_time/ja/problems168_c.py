Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    import sys
    import math

    # 標準入力
    a, b, h, m = map(int, sys.stdin.readline().split())

    # 時針と分針の角度
    angle_h = 360 * (h % 12) / 12 + 360 * m / 12 / 60
    angle_m = 360 * m / 60

    # 時針と分針の角度の差
    angle_diff = abs(angle_h - angle_m)

    # 余弦定理
    # c^2 = a^2 + b^2 - 2ab * cos C
    # c = sqrt(a^2 + b^2 - 2ab * cos C)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(angle_diff)))

    # 出力
    print(c)

=======
Suggestion 2

def main():
    import math
    a, b, h, m = map(int, input().split())
    h = h % 12
    h_angle = 30 * h + 0.5 * m
    m_angle = 6 * m
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    angle = math.radians(angle)
    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle))
    print(ans)

=======
Suggestion 3

def main():
    A, B, H, M = map(int, input().split())
    # 1分あたりの角度
    angle_per_min = 360 / 60
    # 1時間あたりの角度
    angle_per_hour = 360 / 12 / 60
    # 時針の角度
    angle_hour = angle_per_hour * (H * 60 + M)
    # 分針の角度
    angle_min = angle_per_min * M
    # 2本の針の角度差
    angle_diff = angle_hour - angle_min
    # 2本の針の長さの差
    length_diff = (A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(angle_diff))) ** 0.5
    print(length_diff)

=======
Suggestion 4

def main():
    A, B, H, M = map(int, input().split())
    import math
    deg = abs((H*60+M)/2 - M*6)
    if deg > 180:
        deg = 360 - deg
    rad = math.radians(deg)
    ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(rad))
    print(ans)

=======
Suggestion 5

def main():
    a, b, h, m = map(int, input().split())
    angle = abs((h*60+m)/2 - m*6)
    import math
    ans = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(angle)))
    print(ans)
main()

=======
Suggestion 6

def main():
    a,b,h,m = map(int,input().split())
    import math
    #時針の角度
    h_angle = (h*60+m)/720*360
    #分針の角度
    m_angle = m/60*360
    #時針と分針の角度差
    angle = abs(h_angle-m_angle)
    #余弦定理
    c = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(angle)))
    print(c)

=======
Suggestion 7

def solve():
    import sys
    import math

    # 標準入力
    A,B,H,M = map(int, input().split())

    # 時針の角度
    theta_h = H * 30 + M * 0.5
    # 分針の角度
    theta_m = M * 6

    # 2本の針の角度差
    theta = abs(theta_h - theta_m)

    # 2本の針の距離
    # 余弦定理
    ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(theta)))

    # 標準出力
    print(ans)

=======
Suggestion 8

def main():
    A, B, H, M = map(int, input().split())
    import math
    pi = math.pi
    #print(pi)
    #print(A, B, H, M)
    #print(2 * pi / 12 * H)
    #print(2 * pi / 60 * M)
    #print(2 * pi / 12 * H + 2 * pi / 60 * M)
    #print(abs(2 * pi / 12 * H - 2 * pi / 60 * M))
    #print(math.cos(abs(2 * pi / 12 * H - 2 * pi / 60 * M)))
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(abs(2 * pi / 12 * H - 2 * pi / 60 * M))))

=======
Suggestion 9

def main():
    A, B, H, M = map(int, input().split())
    import math
    # 針の角度
    H_angle = 360 * H / 12 + 360 * M / 12 / 60
    M_angle = 360 * M / 60
    # 針の角度差
    angle = abs(H_angle - M_angle)
    # 余弦定理
    ans = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(angle)))
    print(ans)

main()

=======
Suggestion 10

def main():
    import math
    A, B, H, M = map(int, input().split())
    angle = 0
    #角度は時針と分針の角度の差
    angle = abs((H * 60 + M) * 0.5 - M * 6)
    #角度をラジアンに変換
    rad = angle * math.pi / 180
    #余弦定理
    ans = A ** 2 + B ** 2 - 2 * A * B * math.cos(rad)
    print(math.sqrt(ans))
