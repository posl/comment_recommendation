def main():
    a, b, h, m = map(int, input().split())
    print((a**2 + b**2 - 2*a*b*math.cos(math.pi*(h*60+m)/360))**0.5)
main()

if __name__ == '__main__':
    main()