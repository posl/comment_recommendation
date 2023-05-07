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

if __name__ == '__main__':
    main()