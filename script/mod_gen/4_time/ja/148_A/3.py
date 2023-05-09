def main():
    a = int(input())
    b = int(input())
    c = 0
    if a == 1:
        if b == 2:
            c = 3
        elif b == 3:
            c = 2
    elif a == 2:
        if b == 1:
            c = 3
        elif b == 3:
            c = 1
    elif a == 3:
        if b == 1:
            c = 2
        elif b == 2:
            c = 1
    print(c)

if __name__ == '__main__':
    main()