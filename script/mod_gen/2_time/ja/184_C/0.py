def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2:
        print(1)
        return
    if r1 - c1 == r2 - c2:
        print(1)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1 + r2 + c2) % 2 == 0:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if i == 0 or j == 0 or abs(i) == abs(j):
                continue
            if abs(r1 - (r2 + i)) + abs(c1 - (c2 + j)) <= 3:
                print(2)
                return
    print(3)

if __name__ == '__main__':
    main()