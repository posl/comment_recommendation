def main():
    a, b, c, x = map(int, input().split())
    if a < x <= b:
        print(c / (b - a))
    elif x <= a:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()