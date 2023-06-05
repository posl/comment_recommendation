def solve():
    import math
    a,b,h,m = map(int,input().split())
    h_angle = 2*math.pi*(h/12 + m/(12*60))
    m_angle = 2*math.pi*(m/60)
    x = a*math.cos(h_angle) - b*math.cos(m_angle)
    y = a*math.sin(h_angle) - b*math.sin(m_angle)
    print(math.sqrt(x*x + y*y))
