def main():
    a,b = map(int, input().split())
    x = a / pow(a*a+b*b, 0.5)
    y = b / pow(a*a+b*b, 0.5)
    print(x, y)
main()

if __name__ == '__main__':
    main()