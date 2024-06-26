def main():
    a, b, h, m = map(int, input().split())
    h_angle = (h * 60 + m) / 720 * 2 * math.pi
    m_angle = m / 60 * 2 * math.pi
    print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(abs(h_angle - m_angle))))

if __name__ == '__main__':
    main()