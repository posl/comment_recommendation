def main():
    a, b, x = map(int, input().split())
    if x > a**2*b/2:
        print(90 - 2*180*atan(2*(a**2*b-x)/(a**3)))
    else:
        print(90 - 180*atan(2*x/(a*b**2)))

if __name__ == '__main__':
    main()