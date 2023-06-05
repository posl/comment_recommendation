def get_distance(a, b, h, m):
    h_angle = (h + m / 60) * 30
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    return (a ** 2 + b ** 2 - 2 * a * b * cos(angle * pi / 180)) ** 0.5
a, b, h, m = map(int, input().split())
print(get_distance(a, b, h, m))
