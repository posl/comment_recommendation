def main():
    a, b = map(int, input().split())
    c = a + b
    if c == 0:
        print(0)
    elif c == 1:
        print(2)
    elif c == 2:
        print(1)
    elif c == 3:
        print(0)
    elif c == 4:
        print(4)
    elif c == 5:
        print(3)
    elif c == 6:
        print(2)
    elif c == 7:
        print(1)
    elif c == 8:
        print(0)

if __name__ == '__main__':
    main()