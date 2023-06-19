def main():
    a,b,x = map(int,input().split())
    if x <= a*a*b/2:
        print(90 - (x*2)/(a*b*b))
    else:
        print((x*2)/(a*a*a) - 90)

if __name__ == '__main__':
    main()