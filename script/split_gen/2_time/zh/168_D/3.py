def main():
    a, b, h, m = map(int, input().split())
    import math
    pi = math.pi
    h_angle = (h * 60 + m) / 720 * 2 * pi
    m_angle = m / 60 * 2 * pi
    h_x = a * math.cos(h_angle)
    h_y = a * math.sin(h_angle)
    m_x = b * math.cos(m_angle)
    m_y = b * math.sin(m_angle)
    print(math.sqrt((h_x - m_x) ** 2 + (h_y - m_y) ** 2))
