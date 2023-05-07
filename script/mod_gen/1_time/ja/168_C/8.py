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

if __name__ == '__main__':
    main()