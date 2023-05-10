def main():
    n, a, b = map(int, input().split())
    if a == 1:
        print(0)
        return
    if b == 2:
        print(0)
        return
    if n < b:
        print(0)
        return
    if n == a:
        print(0)
        return
    if n == b:
        print(0)
        return
    if n == a+1 and n == b+1:
        print(0)
        return
    if n == a+1 and n != b+1:
        print(1)
        return
    if n == b+1 and n != a+1:
        print(1)
        return
    if n == a+2 and n == b+2:
        print(1)
        return
    if n == a+2 and n != b+2:
        print(2)
        return
    if n == b+2 and n != a+2:
        print(2)
        return
    if n == a+3 and n == b+3:
        print(2)
        return
    if n == a+3 and n != b+3:
        print(3)
        return
    if n == b+3 and n != a+3:
        print(3)
        return
    if n == a+4 and n == b+4:
        print(3)
        return
    if n == a+4 and n != b+4:
        print(4)
        return
    if n == b+4 and n != a+4:
        print(4)
        return
    if n == a+5 and n == b+5:
        print(4)
        return
    if n == a+5 and n != b+5:
        print(5)
        return
    if n == b+5 and n != a+5:
        print(5)
        return
    if n == a+6 and n == b+6:
        print(5)
        return
    if n == a+6 and n != b+6:
        print(6)
        return
    if n == b+6 and n != a+6:
        print(6)
        return
    if n == a+7 and n == b+7:
        print

if __name__ == '__main__':
    main()