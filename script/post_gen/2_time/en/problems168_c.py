Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, h, m = map(int, input().split())
    h_angle = (h + m / 60) * 360 / 12
    m_angle = m * 360 / 60
    angle = abs(h_angle - m_angle)
    c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(angle * math.pi / 180)) ** 0.5
    print(c)

=======
Suggestion 2

def main():
    A, B, H, M = map(int, input().split())
    thetaH = (H * 60 + M) * 360 / (12 * 60)
    thetaM = M * 360 / 60
    theta = abs(thetaH - thetaM)
    ans = (A**2 + B**2 - 2*A*B*math.cos(math.radians(theta))) ** 0.5
    print(ans)

=======
Suggestion 3

def solve():
    A, B, H, M = map(int, input().split())
    h = (H + M / 60) / 12 * 2 * pi
    m = M / 60 * 2 * pi
    d = (A * cos(h) - B * cos(m)) ** 2 + (A * sin(h) - B * sin(m)) ** 2
    print(sqrt(d))

=======
Suggestion 4

def main():
    A, B, H, M = map(int, input().split())
    theta = (H * 60 + M) * 360 / (12 * 60) - M * 360 / 60
    theta = theta / 180 * math.pi
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta)))

=======
Suggestion 5

def main():
    A,B,H,M=map(int,input().split())
    h=30*H+M/2
    m=6*M
    print(((A**2+B**2-2*A*B*math.cos(math.radians(abs(h-m))))**0.5))

=======
Suggestion 6

def main():
    a, b, h, m = map(int, input().split())
    print(solve(a, b, h, m))

=======
Suggestion 7

def main():
    A, B, H, M = map(int, input().split())
    # The hour hand rotates 360 degrees in 12 hours, so it rotates 30 degrees in 1 hour.
    # The minute hand rotates 360 degrees in 60 minutes, so it rotates 6 degrees in 1 minute.
    # The hour hand rotates 30 degrees in 60 minutes, so it rotates 0.5 degrees in 1 minute.
    # The minute hand rotates 6 degrees in 1 hour, so it rotates 0.1 degrees in 1 minute.
    # So, the hour hand rotates 0.5 degrees in 1 minute and the minute hand rotates 0.1 degrees in 1 minute.
    # The hour hand rotates 30 degrees in 1 hour and the minute hand rotates 6 degrees in 1 hour.
    # So, the hour hand rotates 0.5 degrees in 1 hour and the minute hand rotates 0.1 degrees in 1 hour.
    # The hour hand rotates 360 degrees in 12 hours and the minute hand rotates 360 degrees in 60 minutes.
    # So, the hour hand rotates 0.5 degrees in 12 hours and the minute hand rotates 0.1 degrees in 60 minutes.
    # The hour hand rotates 30 degrees in 1 hour and the minute hand rotates 6 degrees in 1 minute.
    # So, the hour hand rotates 0.5 degrees in 1 minute and the minute hand rotates 0.1 degrees in 1 minute.
    # The hour hand rotates 0.5 degrees in 1 minute and the minute hand rotates 0.1 degrees in 1 minute.
    # The hour hand rotates 0.5 degrees in 1 hour and the minute hand rotates 0.1 degrees in 1 hour.
    # The hour hand rotates 0.5 degrees in 12 hours and the minute hand rotates 0.1 degrees in 60 minutes.
    # The hour hand rotates 0.5 degrees in 1 minute and the minute hand rotates 0.1 degrees in 1 minute.
    # The hour hand rotates 0.5 degrees in 1 hour and the minute hand rotates 0.1 degrees in 1 hour.
    # The hour hand rotates 0.5 degrees in 12 hours and the minute hand rotates 0

=======
Suggestion 8

def main():
    a,b,h,m = map(int,input().split())
    # 1時間あたりの角度
    hour_angle = 360/12
    # 1分あたりの角度
    minute_angle = 360/60
    # 総時間
    total_time = h*60 + m
    # 総時間を360°で割ったもの
    total_angle = (total_time/60)*360
    # 時針の角度
    hour_hand_angle = total_angle
    # 分針の角度
    minute_hand_angle = m*minute_angle
    # 時針と分針の角度の差
    angle_difference = abs(hour_hand_angle - minute_hand_angle)
    # 時針と分針の角度の差の長さ
    angle_difference_length = (a**2 + b**2 - 2*a*b*math.cos(math.radians(angle_difference)))**0.5
    print(angle_difference_length)

=======
Suggestion 9

def main():
    import math
    a,b,h,m = map(int,input().split())
    #角度の計算
    h_angle = (h*60 + m) * 0.5
    m_angle = m * 6
    #角度の差
    angle = abs(h_angle - m_angle)
    #角度をラジアンに変換
    rad = math.radians(angle)
    #三平方の定理
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(rad))
    print(c)

=======
Suggestion 10

def main():
    a,b,h,m = map(int,input().split())
    #print(a,b,h,m)

    #1時間を何分にするか
    h_m = 60
    #1時間を何度にするか
    h_d = 360
    #1分を何度にするか
    m_d = 6

    #時針の角度
    h_d += h_d/h_m*m
    #分針の角度
    m_d += m_d*m

    #print(h_d,m_d)

    #時針と分針の角度差
    d = abs(h_d-m_d)
    #print(d)

    #角度をラジアンに変換
    d_rad = d/360*2*math.pi
    #print(d_rad)

    #三角関数を使って答えを求める
    c = math.sqrt(a**2+b**2-2*a*b*math.cos(d_rad))
    print(c)
