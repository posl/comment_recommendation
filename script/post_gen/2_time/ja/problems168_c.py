Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, H, M = map(int, input().split())
    print(calc(A, B, H, M))

=======
Suggestion 2

def main():
    A, B, H, M = map(int, input().split())
    H = H * 60 + M
    H = H * 360 / (60 * 12)
    M = M * 360 / 60
    print(((A**2 + B**2 - 2*A*B*math.cos(math.radians(H-M)))**0.5))

=======
Suggestion 3

def main():
    a, b, h, m = map(int, input().split())
    print((a**2 + b**2 - 2*a*b*math.cos(math.pi*(h*60+m)/360))**0.5)

main()

=======
Suggestion 4

def main():
    a, b, h, m = map(int, input().split())
    # 時針の角度
    theta = 360 / 12 * h + 360 / 12 / 60 * m
    # 分針の角度
    phi = 360 / 60 * m

    # 2つの角度の差
    d = abs(theta - phi)
    # 2つの角度の差が180度以上なら、それを360度から引く
    if d >= 180:
        d = 360 - d

    # 2つの角度の差のラジアン
    rad = d * math.pi / 180
    # 2つの角度の差のラジアンを使って、針の長さを求める
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad)))

=======
Suggestion 5

def main():
    a, b, h, m = map(int, input().split())
    # 時針の角度
    theta_h = (h * 60 + m) / 720 * 360
    # 分針の角度
    theta_m = m / 60 * 360
    # 2 本の針の角度の差
    theta = abs(theta_h - theta_m)
    # 2 本の針の角度の差をラジアンに変換
    theta_rad = theta / 180 * math.pi
    # 2 本の針の角度の差の正弦を求める
    sin_theta = math.sin(theta_rad)
    # 2 本の針の距離を求める
    ans = math.sqrt(a**2 + b**2 - 2 * a * b * sin_theta)
    # 答えを出力
    print(ans)

=======
Suggestion 6

def main():
    import math
    a,b,h,m = map(int,input().split())
    rad = math.pi/2 - (math.pi/6)*h - (math.pi/360)*m
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(rad)))

=======
Suggestion 7

def main():
    import math
    a,b,h,m = map(int,input().split())
    #時針の回転角度
    theta_h = h * 30 + m * 0.5
    #分針の回転角度
    theta_m = m * 6
    #時針と分針の角度の差
    theta = abs(theta_h - theta_m)
    if theta > 180:
        theta = 360 - theta
    ans = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))
    print(ans)

=======
Suggestion 8

def main():
    A, B, H, M = map(int, input().split())
    # 1時間を60分とする
    # 1分を360度とする
    # 1時間を360度とする
    # 1時間を12時間とする
    # 1時間を360度とする
    # 1時間を12時間とする

    # 時針の角度
    theta_H = (360/12) * H + (360/12/60) * M
    # 分針の角度
    theta_M = (360/60) * M
    # 2本の針の角度の差
    theta = abs(theta_H - theta_M)
    # 2本の針の角度の差が180度以上なら、360度から引く
    if theta >= 180:
        theta = 360 - theta
    # 2本の針の角度の差をラジアンに変換
    theta = math.radians(theta)
    # 2本の針の角度の差から、2本の針の端点の距離を求める
    print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(theta)))

=======
Suggestion 9

def main():
    import math

    a, b, h, m = map(int, input().split())
    # h = 0, m = 0
    # h = 1, m = 0
    # h = 0, m = 1
    # h = 1, m = 1

    # 0時0分 -> 0度
    # 1時0分 -> 30度
    # 0時1分 -> 6度
    # 1時1分 -> 36度
    # 1時間 -> 30度
    # 1分 -> 6度

    # 0時0分 -> 0度
    # 1時0分 -> 6度
    # 0時1分 -> 30度
    # 1時1分 -> 36度
    # 1時間 -> 30度
    # 1分 -> 6度

    # 0時0分 -> 0度
    # 1時0分 -> 30度
    # 0時1分 -> 5.5度
    # 1時1分 -> 35.5度
    # 1時間 -> 30度
    # 1分 -> 5.5度

    # 0時0分 -> 0度
    # 1時0分 -> 6度
    # 0時1分 -> 5.5度
    # 1時1分 -> 11.5度
    # 1時間 -> 30度
    # 1分 -> 5.5度

    # 0時0分 -> 0度
    # 1時0分 -> 0度
    # 0時1分 -> 6度
    # 1時1分 -> 6度
    # 1時間 -> 30度
    # 1分 -> 6度

    # 0時0分 -> 0度
    # 1時0分 -> 30度
    # 0時1分 -> 0度
    # 1時1分 -> 30度
    # 1時間 -> 30度
    # 1分 -> 6度

    # 0時0分 -> 0

=======
Suggestion 10

def main():
    A, B, H, M = map(int, input().split())
    # 1時間は、時針の1周に対して、分針の60周に相当する
    # 1分は、時針の1/60周に対して、分針の1周に相当する
    # 1時間は、時針の1周に対して、分針の60周に相当する
    # 1分は、時針の1/60周に対して、分針の1周に相当する
    # 1時間は、時針の1周に対して、分針の60周に相当する
    # 1分は、時針の1/60周に対して、分針の1周に相当する
    # 1時間は、時針の1周に対して、分針の60周に相当する
    # 1分は、時針の1/60周に対して、分針の1周に相当する
    # 1時間は、時針の1周に対して、分針の60周に相当する
    # 1分は、時針の1/60周に対して、分針の1周に相当する
    # 1時間は、時針の1周に対して、分針の60周に相当する
    # 1分は、時針の1/60周に対して、分針の1周に相当する
    # 1時間は、時針の1周に対して、分針の60周に相当する
    # 1分は、時針の1/60周に対して、分針の1周に相当する
    # 1時間は、時針の1周に対して、分針の60周に相当する
    # 1分は、時針の1/60周に対して、分針の1周に相当する
    #
