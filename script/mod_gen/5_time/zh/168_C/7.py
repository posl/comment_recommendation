def clock_distance(a, b, h, m):
    h_angle = h * 30 + m * 0.5
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    angle = angle * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 / 180
    return (a ** 2 + b ** 2 - 2 * a * b * cos(angle)) ** 0.5

if __name__ == '__main__':
    clock_distance()