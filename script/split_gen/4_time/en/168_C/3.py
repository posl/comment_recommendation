def main():
    a,b,h,m = map(int, input().split())
    h_angle = 360*(h/12) + 30*(m/60)
    m_angle = 360*(m/60)
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    angle = math.radians(angle)
    print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle)))
