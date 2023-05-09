def main():
    a, b, c = map(int, input().split())
    print((a*b+b*c+c*a)/(a*b+b*c+c*a-a**2-b**2-c**2))

if __name__ == '__main__':
    main()