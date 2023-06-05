def main():
    a,b,h,m=map(int,input().split())
    import math
    h=h+m/60
    h=h/12
    m=m/60
    m=math.fabs(h-m)
    m=m*2*math.pi
    m=math.cos(m)
    m=math.pow(a,2)+math.pow(b,2)-2*a*b*m
    m=math.sqrt(m)
    print(m)

if __name__ == '__main__':
    main()