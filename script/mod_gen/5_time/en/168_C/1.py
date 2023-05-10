def main():
    import math
    a, b, h, m = map(int, input().split())
    h_angle = (h * 60 + m) / 720 * 360
    m_angle = m / 60 * 360
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))
    print(ans)

if __name__ == '__main__':
    main()