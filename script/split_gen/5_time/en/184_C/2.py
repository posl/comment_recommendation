def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if r1 + c1 == r2 + c2:
        print(1)
        exit()
    if r1 - c1 == r2 - c2:
        print(1)
        exit()
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        exit()
    if (r1 + c1)%2 == (r2 + c2)%2:
        print(2)
        exit()
    if abs(r1 + c1 - r2 - c2) <= 3:
        print(2)
        exit()
    if abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        exit()
    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        exit()
    print(3)
    exit()
