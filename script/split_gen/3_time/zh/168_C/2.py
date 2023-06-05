def main():
    a, b, h, m = map(int, input().split())
    h_angle = (h * 60 + m) / 720 * 360
    m_angle = m / 60 * 360
    angle = abs(h_angle - m_angle)
    import math
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle))))
