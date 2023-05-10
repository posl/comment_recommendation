def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if (r2 - r1) == (c2 - c1) or (r2 - r1) == (c1 - c2) or abs(r2 - r1) + abs(c2 - c1) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            r3 = r1 + i
            c3 = c1 + j
            if r3 == r2 and c3 == c2:
                print(2)
                return
            if (r3 + c3) % 2 == (r2 + c2) % 2:
                print(3)
                return

if __name__ == '__main__':
    main()