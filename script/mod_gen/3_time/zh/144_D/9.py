def main():
    a,b,x = map(int, input().split())
    if a*a*b/2 < x:
        print(90 - 180*2*(a*a*b-x)/(a*a*a))
    else:
        print(180*2*x/(a*b*b))

if __name__ == '__main__':
    main()