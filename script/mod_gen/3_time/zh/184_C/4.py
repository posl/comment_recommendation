def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            r3 = r1 + i
            c3 = c1 + j
            if abs(r3 - r2) + abs(c3 - c2) <= 3:
                print(2)
                return
    print(3)
    return

if __name__ == '__main__':
    main()