def main():
    a,b,h,m = map(int,input().split())
    import math
    #時針の角度
    h_angle = (h*60+m)/720*360
    #分針の角度
    m_angle = m/60*360
    #時針と分針の角度差
    angle = abs(h_angle-m_angle)
    #余弦定理
    c = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(angle)))
    print(c)

if __name__ == '__main__':
    main()