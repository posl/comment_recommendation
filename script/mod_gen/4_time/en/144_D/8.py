def main():
    a,b,x = map(int, input().split())
    if 2*x >= a*a*b:
        print(90 - (90*2*x/(a*a*a - x)))
    else:
        print(90 - (90*2*x/(a*b*b)))

if __name__ == '__main__':
    main()