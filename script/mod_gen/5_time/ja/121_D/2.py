def main():
    a, b = map(int, input().split())
    if a == b:
        print(a)
        return
    if a % 2 == 0:
        if (b - a) % 4 == 1:
            print(1)
        elif (b - a) % 4 == 2:
            print(b)
        elif (b - a) % 4 == 3:
            print(0)
        else:
            print(b)
    else:
        if (b - a) % 4 == 0:
            print(a)
        elif (b - a) % 4 == 1:
            print(1)
        elif (b - a) % 4 == 2:
            print(a ^ b)
        else:
            print(0)

if __name__ == '__main__':
    main()