def main():
    a,b,x = map(int,input().split())
    if x <= a*a*b/2:
        print(math.degrees(math.atan(2*x/(a*a*b))))
    else:
        print(math.degrees(math.atan(2*a*a*b-2*x)/(a*a)))

if __name__ == '__main__':
    main()