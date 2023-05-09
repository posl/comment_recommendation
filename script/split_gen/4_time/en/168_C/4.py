def main():
    a,b,h,m = map(int,input().split())
    h_angle = 2*math.pi*(h/12 + m/12/60)
    m_angle = 2*math.pi*(m/60)
    print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(h_angle - m_angle)))
