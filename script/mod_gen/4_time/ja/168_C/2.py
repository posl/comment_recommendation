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

if __name__ == '__main__':
    main()