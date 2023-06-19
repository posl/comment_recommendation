def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if (r1, c1) == (r2, c2):
        print(0)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for dr in range(-3, 4):
        for dc in range(-3, 4):
            if abs(dr) + abs(dc) != 3:
                continue
            nr, nc = r1 + dr, c1 + dc
            if abs(nr - r2) + abs(nc - c2) <= 3:
                print(2)
                return
    print(3)

if __name__ == '__main__':
    main()