def main():
    a, b, h, m = map(int, input().split())
    # 時針と分針の角度
    h_angle = 30 * h + 0.5 * m
    m_angle = 6 * m
    # 時針と分針の角度差
    angle = abs(h_angle - m_angle)
    # 角度差をラジアンに変換
    rad = angle * math.pi / 180
    # 三平方の定理
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(rad))
    print(c)

if __name__ == '__main__':
    main()