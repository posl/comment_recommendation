def main():
    # 標準入力受け取り
    a, b, h, m = map(int, input().split())
    # 2本の針がなす角度を求める
    # 一般に、時針は1時間で30度、分針は1分で6度動く
    # 0時0分からの時針の角度を求める
    hour_angle = h * 30 + m * 0.5
    # 0時0分からの分針の角度を求める
    minute_angle = m * 6
    # 2本の針がなす角度を求める
    angle = abs(hour_angle - minute_angle)
    # 余弦定理を利用して2本の針の距離を求める
    import math
    distance = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(angle)))
    print(distance)
