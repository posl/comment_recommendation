def main():
    import math
    a,b,d=map(int,input().split())
    if d==360:
        print(a,b)
    else:
        d=d*math.pi/180
        a=a*math.cos(d)-b*math.sin(d)
        b=a*math.sin(d)+b*math.cos(d)
        print(a,b)

if __name__ == '__main__':
    main()