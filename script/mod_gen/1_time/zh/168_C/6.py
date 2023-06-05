def main():
    import math
    a,b,h,m = map(int, input().split())
    h_angle = (h*60 + m) * 0.5
    m_angle = m * 6
    angle = abs(h_angle - m_angle)
    if angle > 180:
        angle = 360 - angle
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(angle)))
    print(c)

if __name__ == '__main__':
    main()