def main():
    import math
    a, b, h, m = map(int, input().split())
    h = h % 12
    h_angle = 30 * h + 0.5 * m
    m_angle = 6 * m
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    angle = math.radians(angle)
    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(angle))
    print(ans)
