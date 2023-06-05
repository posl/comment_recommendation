def main():
    import math
    a,b,h,m = map(int, input().split())
    h_theta = 30*h + 0.5*m
    m_theta = 6*m
    theta = abs(h_theta - m_theta)
    if theta > 180:
        theta = 360 - theta
    theta = theta * math.pi / 180
    print((a**2 + b**2 - 2*a*b*math.cos(theta))**0.5)

if __name__ == '__main__':
    main()