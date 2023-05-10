def main():
    import math
    a,b,h,m = map(int,input().split())
    h_angle = h*30 + m*0.5
    m_angle = m*6
    angle = abs(h_angle-m_angle)
    x = a**2 + b**2 - 2*a*b*math.cos(math.radians(angle))
    print(math.sqrt(x))
