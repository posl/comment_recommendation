def calc_distance(a, b, h, m):
    h_angle = 30 * h + 0.5 * m
    m_angle = 6 * m
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    return (a ** 2 + b ** 2 - 2 * a * b * cos(angle * pi / 180)) ** 0.5
