def main():
    a, b, h, m = map(int, input().split())
    h_angle = (h + m / 60) * 360 / 12
    m_angle = m * 360 / 60
    angle = abs(h_angle - m_angle)
    c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(angle * math.pi / 180)) ** 0.5
    print(c)

if __name__ == '__main__':
    main()