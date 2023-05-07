def main():
    a,b,h,m = map(int,input().split())
    theta = (h*60+m)/720 * 2 * math.pi
    phi = m/60 * 2 * math.pi
    print(math.sqrt(a**2+b**2-2*a*b*math.cos(theta-phi)))

if __name__ == '__main__':
    main()