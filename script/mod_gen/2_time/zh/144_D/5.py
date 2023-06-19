def main():
    a,b,x = map(int,input().split())
    if x > a**2*b/2:
        print(90 - 90*2*x/(a**3-2*x))
    else:
        print(90*x/a**2/b*2)

if __name__ == '__main__':
    main()