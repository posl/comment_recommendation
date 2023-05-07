def main():
    a,b,h,m = map(int,input().split())
    if h == 12:
        h = 0
    if m == 60:
        m = 0
    h_angle = 0.5 * (h*60 + m)
    m_angle = 6 * m
    angle = abs(h_angle - m_angle)
    angle = min(angle, 360 - angle)
    angle = math.radians(angle)
    print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle)))
