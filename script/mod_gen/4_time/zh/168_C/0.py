def main():
    a,b,h,m = map(int,input().split())
    h_angle = (h+m/60)/12*360
    m_angle = m/60*360
    angle = abs(h_angle-m_angle)
    angle = angle if angle<180 else 360-angle
    import math
    angle = angle*math.pi/180
    import decimal
    decimal.getcontext().prec = 100
    print(decimal.Decimal(a**2+b**2-2*a*b*math.cos(angle)).sqrt())

if __name__ == '__main__':
    main()