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

if __name__ == '__main__':
    main()