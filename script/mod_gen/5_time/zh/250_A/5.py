def main():
    h = int(input())
    w = int(input())
    r = int(input())
    c = int(input())
    if h == 1 and w == 1:
        print(0)
        return
    if r == 1 and c == 1:
        print(2)
        return
    if r == h and c == w:
        print(2)
        return
    if r == 1 and c == w:
        print(1)
        return
    if r == h and c == 1:
        print(1)
        return
    if r == 1 or r == h or c == 1 or c == w:
        print(3)
        return
    print(4)

if __name__ == '__main__':
    main()