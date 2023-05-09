def main():
    a,b,h,m=map(int,input().split())
    h=(h+m/60)*2*pi/12
    m=m*2*pi/60
    print(sqrt(a*a+b*b-2*a*b*cos(h-m)))

if __name__ == '__main__':
    main()