Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, h, m = map(int, input().split())
    h_angle = (h + m / 60) * 30
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    angle = math.radians(angle)
    print(math.sqrt(a * a + b * b - 2 * a * b * math.cos(angle)))

=======
Suggestion 2

def main():
    a, b, h, m = map(int, input().split())
    hour_angle = (h * 60 + m) * 360 / (12 * 60)
    minute_angle = m * 360 / 60
    angle = abs(hour_angle - minute_angle)
    angle = min(angle, 360 - angle)
    angle = angle * math.pi / 180
    print(math.sqrt(a * a + b * b - 2 * a * b * math.cos(angle)))

=======
Suggestion 3

def main():
    A, B, H, M = map(int, input().split())
    theta_H = 30 * (H + M / 60)
    theta_M = 6 * M
    theta = abs(theta_H - theta_M)
    print(((A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(theta)))) ** 0.5)

=======
Suggestion 4

def main():
    a,b,h,m = map(int, input().split())
    h_angle = 360*(h/12) + 30*(m/60)
    m_angle = 360*(m/60)
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    angle = math.radians(angle)
    print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle)))

=======
Suggestion 5

def main():
    a,b,h,m = map(int,input().split())
    h_angle = 2*math.pi*(h/12 + m/12/60)
    m_angle = 2*math.pi*(m/60)
    print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(h_angle - m_angle)))

=======
Suggestion 6

def main():
    a,b,h,m=map(int,input().split())
    h=(h+m/60)*2*pi/12
    m=m*2*pi/60
    print(sqrt(a*a+b*b-2*a*b*cos(h-m)))

=======
Suggestion 7

def main():
    import math
    A,B,H,M=map(int,input().split())
    Hrad=math.radians(30*H+0.5*M)
    Mrad=math.radians(6*M)
    Hx=math.cos(Hrad)*A
    Hy=math.sin(Hrad)*A
    Mx=math.cos(Mrad)*B
    My=math.sin(Mrad)*B
    print(math.sqrt((Hx-Mx)**2+(Hy-My)**2))

=======
Suggestion 8

def main():
    A, B, H, M = map(int, input().split())
    # 12時間で360度、1時間で30度、1分で0.5度
    # 時針は分針を巻き込んでいるので、分針の分だけ時針の角度もずれる
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度、0時30分の時針の角度は15度
    # 0時0分の分針の角度は0、0時1分の分針の角度は6度、0時30分の分針の角度は180度
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度、0時30分の時針の角度は15度
    # 0時0分の分針の角度は0、0時1分の分針の角度は6度、0時30分の分針の角度は180度
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度、0時30分の時針の角度は15度
    # 0時0分の分針の角度は0、0時1分の分針の角度は6度、0時30分の分針の角度は180度
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度、0時30分の時針の角度は15度
    # 0時0分の分針の角度は0、0時1分の分針の角度は6度、0時30分の分針の角度は180度
    # 0時0分の時針の角度は0、0時1分の時針の角度は0.5度

=======
Suggestion 9

def main():
    a, b, h, m = map(int, input().split())
    #print(a, b, h, m)
    #print(type(a), type(b), type(h), type(m))

    # 1時間は360度回転する
    # 1分は360度/60回転する
    # 1時間は60分回転する
    # 1分は1/60時間回転する
    # 1時間は1/12時間回転する
    # 1時間は1/12時間回転する
    # 1時間は360度/12回転する
    # 1時間は30度回転する
    # 1分は360度/60回転する
    # 1分は6度回転する
    # 1時間は360度/12回転する
    # 1時間は30度回転する
    # 1時間は360度/12回転する
    # 1時間は30度回転する
    # 1時間は360度/12回転する
    # 1時間は30度回転する

    # 1時間は30度回転する
    # 1分は6度回転する
    # 1時間は30度回転する
    # 1分は6度回転する
    # 1時間は30度回転する
    # 1分は6度回転する
    # 1時間は30度回転する
    # 1分は6度回転する

    # 1時間は360度/12回転する
    # 1時間は30度回転する
    # 1分は360度/60回転する
    # 1分は6度回転する
    # 1時間は360度/12回転する
    # 1時間は30度回転する
    # 1分は360度/60回

=======
Suggestion 10

def main():
    A, B, H, M = map(int, input().split())

    # 1時間は60分なので、1分での角度は360/60=6度
    # 時針は1時間で30度回転なので、1分での角度は30/60=0.5度
    # 分針は1時間で360度回転なので、1分での角度は360/60=6度
    # 時針と分針は1時間で0.5度ずつずれる

    # 1時間は60分なので、1分での角度は360/60=6度
    # 時針は1時間で30度回転なので、1分での角度は30/60=0.5度
    # 分針は1時間で360度回転なので、1分での角度は360/60=6度
    # 時針と分針は1時間で0.5度ずつずれる

    # 時針の角度
    angle_hour = 30 * H + 0.5 * M

    # 分針の角度
    angle_minute = 6 * M

    # 2つの針の角度の差
    angle_diff = abs(angle_hour - angle_minute)

    # 2つの針の角度の差が180度を超えている場合は、
    # 360度から2つの針の角度の差を引いた角度が答え
    if angle_diff > 180:
        angle_diff = 360 - angle_diff

    # 2つの針の角度の差のラジアン
    radian = angle_diff * (3.14159265358979323846 / 180)

    # 2つの針の角度の差のラジアンを使って、
    # 針の長さを使って、2つの針の角度の差の距離を
