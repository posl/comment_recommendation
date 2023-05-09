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

if __name__ == '__main__':
    main()