def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    if r == 1:
        if c == 1:
            print(0)
        elif c == w:
            print(0)
        else:
            print(1)
    elif r == h:
        if c == 1:
            print(0)
        elif c == w:
            print(0)
        else:
            print(1)
    else:
        if c == 1:
            print(1)
        elif c == w:
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    main()