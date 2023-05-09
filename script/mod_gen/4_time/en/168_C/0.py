def main():
    a, b, h, m = map(int, input().split())
    h_angle = (h + m / 60) * 30
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    angle = math.radians(angle)
    print(math.sqrt(a * a + b * b - 2 * a * b * math.cos(angle)))

if __name__ == '__main__':
    main()