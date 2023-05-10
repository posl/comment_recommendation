def main():
    a, b, h, m = map(int, input().split())
    import math
    # 1分で何度進むか
    m_deg = m * 6
    # 1時間で何度進むか
    h_deg = h * 30 + m_deg / 12
    # 2本の針のなす角
    deg = abs(m_deg - h_deg)
    # 余弦定理
    ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(deg)))
    print(ans)
