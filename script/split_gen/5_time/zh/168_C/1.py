def clockHand(a, b, h, m):
    import math
    # 时针转动的角度
    h_angle = 30 * h + 0.5 * m
    # 分针转动的角度
    m_angle = 6 * m
    # 两个指针之间的角度
    angle = abs(h_angle - m_angle)
    # 余弦定理求出两个指针之间的距离
    c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(angle)))
    return c
