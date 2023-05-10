def main():
    import math
    a,b,h,m = map(int,input().split())
    print(math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(30*(h+m/60)-6*m))))

if __name__ == '__main__':
    main()