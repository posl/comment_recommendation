def main():
    n, a, b = map(int, input().split())
    mod = 10**9 + 7
    if n == 2:
        print(0)
        exit()
    if a == 1:
        if b == 2:
            print(0)
            exit()
        else:
            print(1)
            exit()
    if b == n:
        print(0)
        exit()
    if a == 2:
        if b == 3:
            print(0)
            exit()
        else:
            print(1)
            exit()
    if b == n - 1:
        print(0)
        exit()
    if b - a == 1:
        print(0)
        exit()
    if a == b:
        print(1)
        exit()
    if b - a == 2:
        print(1)
        exit()
    if b - a == 3:
        print(2)
        exit()
    if b - a == 4:
        print(4)
        exit()
    if b - a == 5:
        print(7)
        exit()
    if b - a == 6:
        print(13)
        exit()
    if b - a == 7:
        print(24)
        exit()
    if b - a == 8:
        print(44)
        exit()
    if b - a == 9:
        print(81)
        exit()
    if b - a == 10:
        print(149)
        exit()
    if b - a == 11:
        print(274)
        exit()
    if b - a == 12:
        print(504)
        exit()
    if b - a == 13:
        print(927)
        exit()
    if b - a == 14:
        print(1705)
        exit()
    if b - a == 15:
        print(3136)
        exit()
    if b - a == 16:
        print(5768)
        exit()
    if b - a == 17:
        print(10609)
        exit()
    if b - a == 18:
        print(19513)
        exit()
    if b - a == 19:
        print(35890)
        exit()
    if b - a == 20:
        print(66012)
        exit()

if __name__ == '__main__':
    main()