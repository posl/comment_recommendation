def main():
    a, b, h, m = map(int, input().split())
    h_theta = (h + m / 60) * 30
    m_theta = m * 6
    from math import cos, pi
    print((a ** 2 + b ** 2 - 2 * a * b * cos((h_theta - m_theta) / 180 * pi)) ** 0.5)
